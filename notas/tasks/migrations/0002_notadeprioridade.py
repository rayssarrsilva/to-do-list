# Generated by Django 5.1.3 on 2024-11-25 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotadePrioridade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('prioridade', models.CharField(blank=True, choices=[('low', 'Baixa'), ('medium', 'Média'), ('high', 'Alta')], default='prioridade não definida', max_length=6)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
