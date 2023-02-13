from django.db import models


class Categories(models.Model):
    title = models.CharField(
        max_length=64
    )


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
    published = models.BooleanField(
        default=False
    )
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, blank=True, null=True
    )
    rating = models.IntegerField(
        default=0)


class Comments(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )
    text = models.TextField(

    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    publish_date = models.DateTimeField(
        auto_now_add=True
    )
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        default=3
    )


def __str__(self):
    return f'{self.title}'
