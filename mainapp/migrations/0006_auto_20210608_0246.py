# Generated by Django 3.0 on 2021-06-07 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_delete_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('skills_id', models.AutoField(primary_key=True, serialize=False)),
                ('skills_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'Skills',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='MainTask',
        ),
    ]
