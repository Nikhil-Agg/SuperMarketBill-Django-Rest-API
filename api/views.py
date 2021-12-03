from django.shortcuts import render
from .serializers import ItemsSerializer
from .models import items
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'All Items': '/items',
        'Search by Category': '/category',
        'Search by Subcategory': '/subcategory',
        'Add': '/add',
        'Update': '/update'
    }
    return Response(api_urls)

@api_view(['GET'])
def getItems(request):
    if request.query_params:
        print(request.query_params)
        Items=items.objects.filter(**request.query_params.dict())
        print(Items)
        # return Response({})
    else:
        Items = items.objects.all()
    serializer = ItemsSerializer(Items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filterItems(request):
    pass