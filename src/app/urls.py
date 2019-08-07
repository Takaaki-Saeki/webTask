from django.contrib import admin
from django.urls import path, include
from .views import List, Detail, Create, Delete, Update

urlpatterns = [
    path('list/', List.as_view(), name='list'),
    path('detail/<int:pk>', Detail.as_view(), name='detail'),
    path('create/', Create.as_view(), name='create'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
    path('update/<int:pk>', Update.as_view(), name='update'),
]
