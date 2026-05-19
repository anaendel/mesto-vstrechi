from django.db import models

class Feedback(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email')
    subject = models.CharField('Запрос', max_length=200)
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f"{self.name} - ({self.subject})"
