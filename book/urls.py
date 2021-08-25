from django.contrib import admin
from django.urls import path
from book import views


urlpatterns = [
    path('api/', views.BooksListGeneric.as_view()),
    path('add/', views.BooksListCreate.as_view()),
    path('retrive/<int:pk>/', views.BooksListRetrive.as_view()),
    path('update/<int:pk>/', views.BooksListUpdate.as_view()),
    path('delete/<int:pk>/', views.BooksListDel.as_view()),
  
   
]

