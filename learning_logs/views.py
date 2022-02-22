from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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

def new_entry(request, topic_id):
    """ Добавляет записи по конкретной теме"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Если в полученном запросу нет информации - это запрос на пустую форму,
        # данные не обрабатываютсяб создается пустая форма
        form = EntryForm()
    else:
        # При получении запроса POST (с данными) - переданные данные заносятся в форму и 
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # проверка данных на правильность
            new_entry = form.save(commit=False)
            # пока в БД этот экземпляр не заносим
            new_entry.topic = topic
            new_entry.save()
            # А теперь заносим, после привязки этой записи к наименованию темы
            return redirect('learning_logs:topic', topic_id=topic.id)
                # И возвращаемся на страницу этой темы

    # Потом выводим результат - или пустую форму, или недействительную
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)    

def edit_entry(request, entry_id):
    """ Редактирует существующую запись """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Исходный запрос - форма заполняется текущими данными записи
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST, отрабатываются данные
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            # проверка данных на правильность
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
            # правильные данные сохраняем в БД, возвращаемся к странице темы

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context) 




    
