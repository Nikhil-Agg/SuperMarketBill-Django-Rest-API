from django.shortcuts import render
from .serializers import ItemsSerializer
from .models import items
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'All Items': '/items/',
        'Search by Category': '/items/?category=category_name',
        'Search by Subcategory': '/items/?subcategory=category_name',
        'Add': '/add',
        'Update': '/update/pk'
    }
    return Response(api_urls)

@api_view(['GET'])
def getItems(request):
    if request.query_params:
        Items=items.objects.filter(**request.query_params.dict())
    else:
        Items = items.objects.all()

    if Items:
        serializer = ItemsSerializer(Items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def addItems(request):
    if request.method == 'GET':
        Items = {
            "name": "item-name",
            "category": "item-category-name",
            "subcategory": "item-subcategory-name",
            "amount": "item-amount"
        }
        return Response(Items)
    serializer = ItemsSerializer(data=request.data)

    if items.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This data already exists")
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def updateItems(request, pk):
    if request.method == 'GET':
        Items = items.objects.get(pk=pk)
        serializer = ItemsSerializer(Items)
        return Response(serializer.data)

    Item = items.objects.get(id=pk)
    if items.objects.filter(**request.data).exists():
        print('yes')
        raise serializers.ValidationError("This data already exists")
    serializer = ItemsSerializer(instance=Item, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)