from django.db import models

# Create your models here
class Author(models.Model):
    name = models.CharField('Имя автора', max_length=200)
    slug = models.SlugField('Слаг', max_length=200, unique=True, allow_unicode=True)
    photo = models.URLField(
        'Фото', 
        blank=True,
        null=True
    )
    birth_year = models.IntegerField('Год рождения', blank=True, null=True)
    death_year = models.IntegerField('Год смерти', blank=True, null=True)
    biography = models.TextField('Биография', blank=True, null=True)
    is_published = models.BooleanField('Опубликован', default=False) 
    
    class Meta:
        verbose_name = 'автор' 
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name