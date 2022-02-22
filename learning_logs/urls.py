""" Определяет схемы url для приложения learning_logs
"""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех тем
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страничка для того чтоб инициировать новую тему
    path('new_topic/', views.new_topic, name='new_topic'),
    ]
