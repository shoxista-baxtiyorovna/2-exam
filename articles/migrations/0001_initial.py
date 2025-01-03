# Generated by Django 4.2.17 on 2024-12-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('short_content', models.TextField(max_length=300)),
                ('long_content', models.TextField(max_length=500)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
