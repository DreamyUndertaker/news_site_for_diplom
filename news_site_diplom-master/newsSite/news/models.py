from django.db import models


class Category(models.Model):
    name = models.CharField('Категория', max_length=100)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.CharField('Анонс', max_length=100)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='news_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True)

    def __str__(self):
        return f'Новость: {self.title}'

    def get_absolute_url(self):
        return f'news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
