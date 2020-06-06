from django.urls import include, path

from apps.auth.urls import api as auth_urls
from apps.tables.urls import api as tables_urls

app_name = 'api'
urlpatterns = [
    path('auth/', include(auth_urls, namespace='auth')),
    path('tables/', include(tables_urls, namespace='tables')),
]
