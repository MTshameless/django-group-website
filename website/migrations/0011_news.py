# Generated by Django 4.2.4 on 2023-08-05 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_instruments'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('short_description', models.TextField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
