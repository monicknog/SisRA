# Generated by Django 2.0.5 on 2018-06-09 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acesso',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Atualizado em'),
        ),
    ]
