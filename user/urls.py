from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    # path('', views.start, name='start'),
    path('login/', views.login, name='login'),
    # path('ShowPost/', views.ShowPost, name='showpost'),
    # path('ShowPost/<int:pk>/', views.ShowText, name='showtext'),
    path('test/', views.Test),
    # path('posting/', views.Posting, name='post_new'),
    path('register/', views.Register, name='register'),
    path('chordrppr/', views.ChoiceOrderPaper, name='chordrppr'),
    path('catchitems/', views.CatchItemAjax, name='aa'),
    path('additem/', views.AddItem, name='additem'),
    path('catchorderpaper/', views.CatchOrderPaperAjax, name='catchorderpaper'),
    path('resultone/', views.ResultOne, name='resultone'),
    path('resulttwo/', views.ResultTwo, name='resulttwo'),
    path('marrydata/', views.MarryData, name='marrydata'),
]
