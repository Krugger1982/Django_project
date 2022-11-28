from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        # не генерировать подпись для текстового поля


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry'}
        # Для текстового поля генерируется подпись "Entry"
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        # Это элемент формы - поле для ввода данных.
        # Сюда пользователь будет вводить текстовый материал по теме
