from django.db import models

class Topic(models.Model):
    """ Тема, которую изучаю """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Вохвращает строковое предсавение модели """
        return self.text


class Entry(models.Model):
    """ Информация по теме """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """ Вохвращает строковое предсавение модели """
        return f"{self.text[:50]}..."
