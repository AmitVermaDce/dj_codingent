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
from django.urls import path
from accounts.views import (
    login_view,
    login_view_auth,
    logout_view,
    register_view,
    check_username,
)

app_name = "accounts"
urlpatterns = [
    path('login/', login_view, name="login"),
    path('login1/', login_view_auth, name="login1"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
]

# HTMX urls

htmx_urlpatterns = [
    path("check_username/", check_username, name="check_username"),
]

urlpatterns += htmx_urlpatterns
