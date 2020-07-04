# Generated by Django 2.2.13 on 2020-06-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]
