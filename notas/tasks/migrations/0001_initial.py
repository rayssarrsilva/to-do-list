# Generated by Django 5.1.3 on 2024-11-24 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
