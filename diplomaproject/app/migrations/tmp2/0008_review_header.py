# Generated by Django 2.2.16 on 2020-10-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20201005_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='header',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
    ]