from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('v1/token/access/', TokenObtainPairView.as_view()),
    path('v1/token/refresh/', TokenRefreshView.as_view()),
]