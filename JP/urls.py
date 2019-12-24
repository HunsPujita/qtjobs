"""JP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from jobs import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jsonreglist/', views.register_list),
    path('jsonloginlist/', views.login_list),
    path('jsonresumelist/', views.resume_list),
    path('jsonusertypelist/', views.usertypelist),
    path('jsongenderlist/', views.genderlist),
    path('enterregister', views.register),
    path('createlogin', views.create_login),
    path('enterresume', views.resume),
    path('credlogin', views.login),
    path('registerform/', views.reg),
    path('loginform/', views.log),
    path('resumeform/', views.res),
    path('registertable/', views.reg_table),
    path('resumetable/', views.res_table),
    path('logintable/', views.log_table),
    path('upload', views.upload)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)