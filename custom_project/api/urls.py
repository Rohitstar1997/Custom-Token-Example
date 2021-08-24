from django.urls import path, include, re_path
from . import views
urlpatterns = [
    path('', views.HelloView.as_view()),
    path('create/', views.ForestCreateView.as_view()),
    path('list/', views.ForestListView.as_view()),
]
