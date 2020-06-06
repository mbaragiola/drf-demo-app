from django.urls import include, path

from rest_framework.routers import DefaultRouter

from apps.auth import views
from apps.auth.views.jwt import (
    ObtainJSONWebToken,
    RefreshJSONWebToken,
    VerifyJSONWebToken,
)

router = DefaultRouter()
router.register("logout", views.LogoutViewSet, basename="logout")

app_name = "auth"
urlpatterns = [
    path(
        "login/",
        view=views.LoginView.as_view(),
        name='login'
    ),
    path('obtain-jwt-token/', ObtainJSONWebToken.as_view(), name='get-jwt-token'),
    path('refresh-jwt-token/', RefreshJSONWebToken.as_view()),
    path('verify-jwt-token/', VerifyJSONWebToken.as_view()),
    path("", include(router.urls))
]
