# Generated by Django 4.2.14 on 2024-07-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_task_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='urgent',
            field=models.BooleanField(default=False),
        ),
    ]
