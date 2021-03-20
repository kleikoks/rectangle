from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import WasteUtil
from django.shortcuts import get_object_or_404
from .serializers import WasteUtilSerializer
from rest_framework.views import APIView

# LIST
class WasteUtilListView(APIView):
    def get(self, request):
        queryset = WasteUtil.objects.all()
        serializer = WasteUtilSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def list_waste_util(request):
    queryset = WasteUtil.objects.all()
    serializer = WasteUtilSerializer(queryset, many=True)
    return Response(serializer.data)

# OBJECT
class WasteUtilDetailView(APIView):
    def get(self, request, pk):
        queryset = WasteUtil.objects.get(pk=pk)
        serializer = WasteUtilSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def get(request, pk):
    queryset = WasteUtil.objects.get(pk=pk)
    serializer = WasteUtilSerializer(queryset, many=True)
    return Response(serializer.data)