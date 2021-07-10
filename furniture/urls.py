from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_furniture, name='furniture'),
    path('<int:furniture_id>/', views.furniture_detail, name='furniture_detail'),
]