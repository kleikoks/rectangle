from django.http import request
from ..models import *
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse

from django.conf import settings

def get_available_text(request):
    pk = request.GET.get('id')
    text_resource = get_object_or_404(Text, pk=pk)
    languages = set_language_list()
    response = {}
    for language in languages:
        exec_response = {}
        command = f'text = text_resource.text.text_{language}'
        exec(command, {'text_resource': text_resource}, exec_response)
        response[f'text_{language}'] = exec_response['text']
    return JsonResponse(response)

def set_language_list():
    languages_list = []
    for language in settings.LANGUAGES:
        languages_list.append(language[0])
    return languages_list
