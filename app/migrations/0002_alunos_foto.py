# Generated by Django 5.0.6 on 2024-05-08 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunos',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
