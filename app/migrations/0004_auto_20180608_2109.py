# Generated by Django 2.0.4 on 2018-06-09 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180608_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acesso',
            old_name='updated_at',
            new_name='atualizado_em',
        ),
    ]