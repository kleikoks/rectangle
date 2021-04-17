from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('', include('translation.urls')),
    path('', include('dj_users.urls')),
    path('api/', include('dj_rest_framework.api.urls')),
    path('api/', include('translation.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += i18n_patterns(
    path('', index, name='index'),
    prefix_default_language = False
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)