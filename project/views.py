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




from django.apps import apps

@api_view(['GET'])
def book_list(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)

    return Response(serializer.data)

def index(request):
    book = TextResource.objects.first()
    exec("book.text.text_ru = 'RU'")
    # book.text.text_ru = 'RU'
    text = Text.objects.first()
    return render(request, 'project/index.html', locals())

def set_lang(request, lang):
    redirect_to = f'/{lang}'
    prev_url = request.META.get('HTTP_REFERER', '')
    if prev_url:
        splitted = prev_url.split('/')
        splitted[3] = lang
        if settings.LANGUAGE_CODE == lang:
            splitted.remove(lang)
        redirect_to = str('/').join(splitted)
    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang
    # print(request.META.get('HTTP_ACCEPT_LANGUAGE'))
    return HttpResponseRedirect(redirect_to)