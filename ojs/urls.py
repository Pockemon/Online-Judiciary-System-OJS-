"""ojs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    #path('',include('page.urls')),
    path('admin/', admin.site.urls),
    path('',include('page.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/signup/', page.SignUpView.as_view(), name='reg_form'),
    #path('accounts/signup/victim/', victims.VictimSignUpView.as_view(), name='victim_signup'),
    #path('accounts/signup/lawyer/', lawyers.LawyerSignUpView.as_view(), name='lawyer_signup'),
    #path('accounts/signup/police/', polices.PoliceSignUpView.as_view(), name='police_signup'),
    #path('page/',include('django.contrib.auth.urls')),
    #path('page/')
    #path('page/',include('page.urls')),
    #path('accounts/',include('accounts.urls')),
]
