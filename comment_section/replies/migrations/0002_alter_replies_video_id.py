# Generated by Django 3.2.7 on 2021-09-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replies',
            name='video_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
