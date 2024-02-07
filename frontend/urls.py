from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="home"),
    path("<int:questionaire_id>/", views.questionaire_page, name="questionaire_page"),
    path("login", views.login_page, name="login"),
]
