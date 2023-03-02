from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET'])
def super_list(request):
    
    if request.method == 'GET':
        supers =  Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def super_detail(request, pk):

    if request.method == 'GET':
        super = get_object_or_404(Super, pk=pk)
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    

 