from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.CharField('Анонс', max_length=100)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='news_images/', null=True, blank=True)

    def __str__(self):
        return f'Новость: {self.title}'

    def get_absolute_url(self):
        return f'news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
