from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from animals.models import Animals
from animals.serializers import AnimalsSerializer



class AnimalsView(APIView):
    def get(self, _: Request):
        animals = Animals.objects.all()
        serialized = AnimalsSerializer(instance=animals, many=True)
        return Response({"animals": serialized.data}, status.HTTP_200_OK)

    def post(self, request: Request):
        serialized = AnimalsSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        try:
            serialized.save()
            return Response(serialized.data, status.HTTP_201_CREATED)
        except ValueError as error:
            return Response(*error.args)

class AnimalsIdView(APIView):
    def get(self,_:Request, id:int):
        animals = get_object_or_404(Animals,pk=id)
        serialized = AnimalsSerializer(animals)

        return Response(serialized.data,status.HTTP_200_OK)
    
    def patch(self,request:Request, id:int):
        try:
            animals = get_object_or_404(Animals,pk=id)
            serialized = AnimalsSerializer(animals,request.data, partial=True)
            serialized.is_valid(raise_exception=True)
            serialized.save()

            return Response(serialized.data,status.HTTP_200_OK)
        except Http404:
            return Response({"detail": "Animal not found."}, status.HTTP_404_NOT_FOUND)

        except KeyError as err:
            return Response(*err.args)

    def delete(self,_:Request, id:int):
        animals = get_object_or_404(Animals,pk=id)
        animals.delete()
        return Response("",status.HTTP_204_NO_CONTENT)
