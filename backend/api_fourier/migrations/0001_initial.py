# Generated by Django 4.1 on 2022-11-05 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='documentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.TextField(max_length=250)),
                ('title', models.TextField(max_length=250)),
                ('body', models.TextField(max_length=2000)),
            ],
        ),
    ]
