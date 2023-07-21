"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from .views import home_view

from accounts.views import (
    login_view,
    login_view_auth,
    logout_view,
    register_view,
)

urlpatterns = [
    path('', home_view),
    path("recipes/", include("recipes.urls")),
    path("articles/", include("articles.urls")),   
    path('admin/', admin.site.urls),
    path('accounts/login/', login_view),
    path('accounts/login1/', login_view_auth),
    path('accounts/logout/', logout_view),
    path('accounts/register/', register_view),
]
