from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length=64, verbose_name='Заголовок'
    )
    text = models.TextField()
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    publish_date = models.DateTimeField(
        auto_now_add=True
    )
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

