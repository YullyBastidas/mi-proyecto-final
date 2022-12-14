# Generated by Django 4.1.2 on 2022-10-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_blog', models.CharField(max_length=14)),
                ('construido_por', models.CharField(max_length=30)),
                ('titulo_principal', models.CharField(default='', max_length=30)),
                ('subtitulo_principal', models.CharField(default='', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_content', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=3000)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
