from django.urls import path
from crawl import views

app_name = "crawl"

urlpatterns = [
    path('', views.home, name="home"),
    path('results/', views.searched, name="searched"),
    path('test/',views.test),
    path('<str:slug>/', views.code, name="code"),

]
