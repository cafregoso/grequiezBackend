# Generated by Django 4.0.5 on 2022-06-27 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('content1', models.TextField(verbose_name='Contenido principal')),
                ('content2', models.TextField(blank=True, verbose_name='Parrafo opcional')),
                ('content3', models.TextField(blank=True, verbose_name='Parrafo opcional')),
                ('resume', models.TextField(blank=True, verbose_name='Resumen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('principla_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]