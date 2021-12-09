# Generated by Django 3.2.9 on 2021-12-09 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete', 'later']},
        ),
        migrations.AddField(
            model_name='task',
            name='later',
            field=models.BooleanField(default=False),
        ),
    ]
