from django.urls import path
from . import views

urlpatterns = [
    path('dashboard_laporan_kasus', views.home_dashboard, name='dashboard_laporan_kasus'),
]