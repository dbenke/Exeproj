from django.urls import path
from . import views


urlpatterns = [
 path("", views.home, name="home"),
 path("logout/", views.logout_user, name="logout"),
 path("musculo/", views.musculo, name="musculo"),
 path("laminas/", views.laminas, name="laminas"),
 path("record/<int:pk>", views.customer_record, name="record"),
 
 path("register/", views.register_user, name="register"),
 path("adicionar/", views.adicionar, name="adicionar"),
 path("sala/", views.sala, name="sala"),
 
 path("sala/<str:room_name>/", views.room, name="room"),
]

