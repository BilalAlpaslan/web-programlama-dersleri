from django.contrib import admin
from django.urls import path
from .views import home,detail

urlpatterns = [
    path('article/<slug:slug>',detail,name="detail"),
    path('', home )
]