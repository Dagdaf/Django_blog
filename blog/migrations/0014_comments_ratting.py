# Generated by Django 4.1.3 on 2023-02-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_comments_ratting'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='ratting',
            field=models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=1),
            preserve_default=False,
        ),
    ]
