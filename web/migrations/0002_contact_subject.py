# Generated by Django 4.2.3 on 2023-11-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
