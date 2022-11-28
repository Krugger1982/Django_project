""" Определяет схемы УРЛов для пользователей """

from django.urls import include, path

from . import views

app_name = 'users'

urlpatterns = [
    # Включить URL авторизации - по умолчанию
    # из этого модуля автоматически берутся странички log_in и log_out
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации
    path('register/', views.register, name='register'),
    ]
