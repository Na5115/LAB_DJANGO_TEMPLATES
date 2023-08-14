from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path('today/',views.today_view, name="today_view"),
    path('random/password/',views.random_view, name="random_view"),
    path('favs/games/',views.games_view, name="games_view"),


]