# Generated by Django 4.2 on 2023-08-17 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
