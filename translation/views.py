from django.conf import settings
from django.utils import translation
from django.shortcuts import HttpResponseRedirect

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