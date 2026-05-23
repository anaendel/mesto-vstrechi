from django.db import models

class Material(models.Model):
    title = models.CharField('Название', max_length=200)
    url = models.TextField('Ссылка')
    order = models.IntegerField('Порядок', default=0)
    is_published = models.BooleanField('Опубликован', default=True)

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'Материалы'
        ordering = ['order']
        
    def __str__(self):
        return self.title
