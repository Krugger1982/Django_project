from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Регистрирует нового пользователя"""
    if request.method != 'POST':
        # Выведется пустая регистрационная форма
        form = UserCreationForm()
    else:
        # Обработка заполенной формы
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Одновременно с сохранением нового пользователя
            # будет очцществлен вход для него и переход на главную
            login(request, new_user)
            return redirect('learning_logs:index')
    # Вывод устой или недействительной формы
    context = {'form': form}
    return render(request, 'registration/register.html', context)
