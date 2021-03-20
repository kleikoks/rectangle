from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import WasteUtil
from django.shortcuts import get_object_or_404
from .serializers import WasteUtilSerializer, WasteUtilReviewSerializer
from rest_framework.views import APIView

@api_view(['GET',])
def list_waste_util(request):
    queryset = WasteUtil.objects.all()
    serializer = WasteUtilSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def detail_waste_util(request, pk):
    queryset = WasteUtil.objects.get(pk=pk)
    serializer = WasteUtilSerializer(queryset)
    return Response(serializer.data)

@api_view(['POST',])
def create_waste_util_review(request):
    item = WasteUtilReviewSerializer(data=request.data)
    if item.is_valid():
        item.save()
    return Response(status=201)



# @api_view(['GET',])
# def detail_wasteutil(request, id):
#     try:
#         item = WasteUtil.objects.get(pk=id)
#     except:
#         Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = WasteUtilSerializer(WasteUtil)
#     return Response(serializer.data)

# @api_view(['PUT',])
# def update_wasteutil(request):
#     serializer = WasteUtilSerializer(WasteUtil, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         data = {'response': 'OK'}
#         return Response(data=data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE',])
# def del_wasteutil(request):
#     operation = WasteUtil.objects.first().delete()
#     if operation:
#         data = {'response': 'OK'}
#         return Response(data=data)
#     return Response(status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST',])
# def del_wasteutil(request):
#     item = WasteUtil(name='ff pls')
#     serializer = WasteUtilSerializer(item, data=request.data)
#     if serializer.is_valid():
#         data = {'response': 'OK'}
#         return Response(data=data)
#     return Response(status=status.HTTP_400_BAD_REQUEST)