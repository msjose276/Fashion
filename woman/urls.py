from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListOfClothing, name='clothing'),
    path('<str:keyword>/', views.ItemDetail, name='item_detail'),

    #path('african gucci/', views.ItemDetail, name='item_detail'),

]