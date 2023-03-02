from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET', 'POST'])
def super_list(request):
    
    if request.method == 'GET':
        super_category = request.query_params.get('super_type')
        #supers =  Super.objects.all()
        queryset = Super.objects.all()
        custom_response_dictionary = {}
        if super_category:
            queryset = queryset.filter(super_type__type=super_category)
        serializer = SuperSerializer(queryset, many=True)
        queryset = Super.objects.all()
        heroes = queryset.filter(super_type__type = "hero")
        villains = queryset.filter(super_type__type = "villain")
        heroes_serialized =SuperSerializer(heroes,many=True)
        villains_serialized =SuperSerializer(villains,many=True)
        custom_dictionary_response = {
            "Heroes": heroes_serialized.data,
            "Villains": villains_serialized.data
        }
        return Response(custom_dictionary_response)
    
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        #super = get_object_or_404(Super, pk=pk)
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        #super = get_object_or_404(serializer, pk=pk)
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

 