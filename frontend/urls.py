from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="home"),
    path("create-questionaire/", views.create_questionaire, name="create"),
    path("<int:questionaire_id>", views.questionaire_page, name="questionaire_page"),
    path("login", views.login_page, name="login"),
]
