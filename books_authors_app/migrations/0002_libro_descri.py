# Generated by Django 3.2.5 on 2021-08-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='descri',
            field=models.TextField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
