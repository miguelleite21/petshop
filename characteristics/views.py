from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from characteristics.models import Characteristics
from characteristics.serializers import CharacteristicsSerializer



class CharacteristicsView(APIView):
    def get(self, _: Request):
        characteristics = Characteristics.objects.all()
        serialized = CharacteristicsSerializer(instance=characteristics, many=True)
        return Response({"characteristics": serialized.data}, status.HTTP_200_OK)

    def post(self, request: Request):
        serialized = CharacteristicsSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        try:
            serialized.save()
            return Response(serialized.data, status.HTTP_201_CREATED)
        except ValueError as error:
            return Response(*error.args)

class CharacteristicsIdView(APIView):
    def delete(self,_:Request, id:int):
        characteristics = get_object_or_404(Characteristics,pk=id)
        characteristics.delete()
        return Response("",status.HTTP_204_NO_CONTENT)
