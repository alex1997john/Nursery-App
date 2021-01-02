"""nursary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .api import OrderCreateApi, OrdersApi, PlantApi, PlantCreateApi, PlantsApi, RegisterApi, UserApi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register', RegisterApi.as_view()),
    path('api/user', UserApi.as_view()),
    path('api/plants', PlantsApi.as_view()),
    path('api/plant/<int:id>', PlantApi.as_view()),
    path('api/plant/create', PlantCreateApi.as_view()),
    path('api/orders', OrdersApi.as_view()),
    path('api/order', OrderCreateApi.as_view()),
]
