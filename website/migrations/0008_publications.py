# Generated by Django 4.2.4 on 2023-08-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_rename_authers_representativepublications_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('authors', models.TextField()),
                ('doi', models.CharField(max_length=100)),
                ('journal', models.CharField(max_length=100)),
                ('publish_year', models.CharField(max_length=100)),
                ('publish_issue', models.CharField(max_length=100)),
                ('publish_page', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'publications',
            },
        ),
    ]