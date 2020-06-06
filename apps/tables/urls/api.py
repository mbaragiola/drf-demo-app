from django.urls import include, path

from rest_framework.routers import DefaultRouter

from apps.tables import views

router = DefaultRouter()

router.register("tables", views.TableViewSet, basename="table")

app_name = "tables"
urlpatterns = [
    path(
        "tables/<str:table_name>/entries/",
        views.EntriesByTableList.as_view(),
        name='entry-list'
    ),
    path(
        "tables/<str:table_name>/query/",
        views.QueryTableView.as_view(),
        name='entry-query'
    ),
    path("", include(router.urls))
]
