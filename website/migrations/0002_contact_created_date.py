# Generated by Django 2.2.13 on 2020-07-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
