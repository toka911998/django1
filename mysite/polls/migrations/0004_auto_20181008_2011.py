# Generated by Django 2.1.2 on 2018-10-08 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_article_thumb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thumb',
            new_name='image',
        ),
    ]
