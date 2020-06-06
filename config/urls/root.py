from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from config.urls import api

urlpatterns = [
    path('api/', include(api, namespace='api')),
]

if settings.BACKOFFICE:
    urlpatterns += [
        # Django Admin, use {% url 'admin:index' %}
        path('admin/', admin.site.urls),
    ]

if settings.DEBUG:
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi
    from rest_framework.permissions import AllowAny

    schema_view = get_schema_view(
        openapi.Info(
            title="Moni Colombia API",
            default_version='v1'
        ),
        public=True,
        permission_classes=(AllowAny,)
    )
    urlpatterns += [
        path(
            'swagger/',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'
        ),
    ]
