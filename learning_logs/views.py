from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

def index(request):
    """ Домашняя страница для приложения learning_logs
    """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Представление для формирования странички со списком всех тем
    """
    topics = Topic.objects.order_by('date_added')
    # извлекаем все темы из БД в переменную, сортируем по дате
    context = {'topics':topics}
    # этот словарь нужен чтоб избежать перечисления аргументов для функции render
    
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Представляет страничку с конкретной темой и все записи по ней
    """
    topic = Topic.objects.get(id=topic_id)
    # извлекаем из БД конкретную тему в переменную topic
    entries = topic.entry_set.order_by('-date_added')
    # и извлекаем из БД все записи по этой теме
    context = {'topic':topic, 'entries':entries}

    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """ Для вывода странички с формой чтоб начать новую тему
    """
    if request.method != 'POST':
        # Если данные не отправлялись, создается пустая форма
        form = TopicForm()
    else:
        # Если в запросе переданны данные, то обрабатывается заполненная форма
        form = TopicForm(data=request.POST)
        if form.is_valid():
        # проверяется введенная информация
            form.save()
            # щаписываем ее в БД
            # и переадресовываем пользователя назад на список тем
            return redirect('learning_logs:topics')

    # Потом выводим результат - или пустую форму, или недействительную
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
