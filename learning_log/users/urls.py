""" Определяет схемы УРЛов для пользователей """

from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # Включить URL авторизации - по умолчанию
    # из этого модуля автоматически берутся странички log_in и log_out
    path('', include('django.contrib.auth.urls')),
    
    ]
