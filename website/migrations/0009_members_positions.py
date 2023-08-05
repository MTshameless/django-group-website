# Generated by Django 4.2.4 on 2023-08-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_publications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('homeland', models.CharField(max_length=100)),
                ('hobby', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='members')),
            ],
            options={
                'verbose_name_plural': 'members',
            },
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('member', models.ManyToManyField(to='website.members')),
            ],
            options={
                'verbose_name_plural': 'positions',
            },
        ),
    ]
