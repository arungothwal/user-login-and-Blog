# Generated by Django 3.0.4 on 2020-03-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
