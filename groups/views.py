from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from groups.models import Groups
from groups.serializers import GroupsSerializer



class GroupsView(APIView):
    def get(self, _: Request):
        groups = Groups.objects.all()
        serialized = GroupsSerializer(instance=groups, many=True)
        return Response({"groups": serialized.data}, status.HTTP_200_OK)

    def post(self, request: Request):
        serialized = GroupsSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data, status.HTTP_201_CREATED)
        
class GroupsIdView(APIView):
    
    def get(self,_:Request, id:int):
        groups = get_object_or_404(Groups,pk=id)
        serialized = GroupsSerializer(groups)

        return Response(serialized.data,status.HTTP_200_OK)
    
    def patch(self,_:Request, id:int):
        groups = get_object_or_404(Groups,pk=id)
        serialized = GroupsSerializer(groups,Request.data, partial=True)
        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data,status.HTTP_204_NO_CONTENT)


    def delete(self,_:Request, id:int):
        groups = get_object_or_404(Groups,pk=id)
        groups.delete()
        return Response("",status.HTTP_204_NO_CONTENT)
        