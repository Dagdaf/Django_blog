# Generated by Django 4.1.3 on 2023-02-13 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_comments_ratting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='ratting',
        ),
    ]
