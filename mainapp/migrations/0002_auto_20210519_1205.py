# Generated by Django 3.0 on 2021-05-19 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='blog_category',
        ),
        migrations.AlterModelOptions(
            name='direction',
            options={},
        ),
        migrations.DeleteModel(
            name='BlogCategory',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
