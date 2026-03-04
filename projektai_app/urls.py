from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjektasView.as_view()),
    path('projektai/<int:pk>', views.ProjektasDetailView.as_view()),
]
