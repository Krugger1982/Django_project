# Learning log
Это небольшой блог для личных записей.
Создан в формате веб-сайта.

### Использованные технологии:

Python - 3.7
Django - 2.2.27
sqlite



## Установка

Чтоб развернуть проект на локальной машине клонируйте репозиторий 

```git clone git@github.com:Krugger1982/Django_project.git```

#### Установите и активируйте виртуальное окружение.  

Cоздание виртуального окружения:  
```
$ python3 -m venv venv
```

Активация виртуального окружения:  
```$ source venv/bin/activate``` (команда для Linux/MacOS)  
или:  
```$ source venv/Scripts/activate``` (команда для Windows)  

при активированном виртуальном окружении выполните команду: 

```$ pip install -r requirements.txt ```


# Запуск сервера на локальной машине 
В папке Django_project/learning_log/ выполните команду запуска сервера:  

```$ python3 manage.py runserver ```  

Сервер запустится по адресу: http://127.0.0.1
Зарегистрируйтесь на сайте.
Перейдите на вкладку "Темы"

# Работа с сервисом:
Сервис преставляет из себя электронный дневник.
Структура:

Тема 1 | -  запись № 1
       | -  запись № 2
       | -  запись № 3
       
Тема 2 | -  запись № 1
       | -  запись № 2
       ...
       
Вы можете начинать новые темы по изучаемому предмету, добавлять/корректировать/удалять записи в имеющихся темах.

Автор: [Алексей Разумовский](https://vk.com/razumovsky1982) 
