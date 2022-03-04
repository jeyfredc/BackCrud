from django.contrib import admin
from django.urls import path
from .users import createUsers, getUsers, updateUsers, deleteUsers

urlpatterns = [
    path('createUsers', createUsers),
    path('getUsers', getUsers),
    path('editUsers/<int:nrodocumento>', updateUsers),
    path('delete/<int:nrodocumento>', deleteUsers),
]