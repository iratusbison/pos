"""EpPos2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from pos.views import login
from django.urls import path , include

urlpatterns = [
    path('', RedirectView.as_view(url='/pos', permanent=True)),
    path('pos/', include('pos.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),
        {'next_page': '/pos/order'}, name='logout'),
    path('accounts/login/', login, name='login'),
]
