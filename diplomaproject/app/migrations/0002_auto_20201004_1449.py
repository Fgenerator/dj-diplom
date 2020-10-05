# Generated by Django 2.2.16 on 2020-10-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='media',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=None, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.DeleteModel(
            name='ProductCategoryInfo',
        ),
    ]
