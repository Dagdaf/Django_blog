# Generated by Django 4.1.3 on 2023-02-13 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_post_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='rating',
        ),
    ]
