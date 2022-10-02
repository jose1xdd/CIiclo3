"""ciclo3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from medicli import views


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('paciente/', views.PacienteList.as_view()),
    path('paciente/<str:pk>/', views.PacienteDetail.as_view()),
    path('medico/', views.MedicoList.as_view()),
    path('medico/<str:pk>/', views.MedicoDetail.as_view()),
    path('enfermero/', views.EnfermeroList.as_view()),
    path('enfermero/<str:pk>/', views.EnfermeroDetail.as_view()),
    path('familiar/', views.FamiliarList.as_view()),
    path('familiar/<str:pk>/', views.FamiliarDetail.as_view()),
    path('diagnostico/', views.DiagnosticoList.as_view()),
    path('diagnostico/<int:pk>/', views.DiagnosticoDetail.as_view()),
    path('signos_vitales/', views.Signos_vitalesList.as_view()),
    path('signos_vitales/<int:pk>/', views.Signos_vitalesDetail.as_view()),
    path('historia_clinica/', views.Historia_clinicaList.as_view()),
    path('historia_clinica/<int:pk>/', views.Historia_clinicaDetail.as_view()),
]
