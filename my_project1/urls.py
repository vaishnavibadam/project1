from django.conf.urls import url
from my_project1 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
