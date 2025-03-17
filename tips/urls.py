# server/taxi/urls.py

from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('api/log_in/', views.LogInView.as_view(), name='log_in'), # new
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # new
]