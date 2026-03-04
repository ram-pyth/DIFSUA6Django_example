from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjektasView.as_view()),
]
