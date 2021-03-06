from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_furniture,
         name='furniture'),
    path('<int:furniture_id>/',
         views.furniture_detail, name='furniture_detail'),
    path('add/', views.add_furniture,
         name='add_furniture'),
    path('edit/<int:furniture_id>/', views.edit_furniture,
         name='edit_furniture'),
    path('delete/<int:furniture_id>/', views.delete_furniture,
         name='delete_furniture'),
]
