# Generated by Django 3.2.5 on 2023-04-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('standBy', 'standBy'), ('published', ' published'), ('removed', 'removed')], default='standBy', max_length=10),
        ),
    ]
