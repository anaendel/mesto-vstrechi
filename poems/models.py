from django.db import models

from authors.models import Author

class Poem(models.Model):
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,
        related_name='poems',
        verbose_name='Автор'
        )
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('Слаг', max_length=200, unique=True, allow_unicode=True)
    preview = models.TextField('Превью')
    text = models.TextField('Текст')
    year = models.IntegerField('Год', blank=True, null=True)
    is_published = models.BooleanField('Опубликовано', default=False)

    class Meta:
        verbose_name = 'стихотворение'
        verbose_name_plural = 'Стихотворения'

    def __str__(self):
        return self.title
 