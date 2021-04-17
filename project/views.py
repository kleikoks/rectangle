from .models import *
from django.shortcuts import render
from rest_framework.decorators import api_view
from . serializers import BookSerializer
from rest_framework.response import Response
from django.http import HttpResponseRedirect

from django.utils import translation
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.urls import reverse
from django.conf import settings

import xml
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import csv
import pathlib



from django.apps import apps

@api_view(['GET'])
def book_list(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)

    return Response(serializer.data)

def index(request):
    return render(request, 'project/index.html', locals())
