# Generated by Django 4.1.1 on 2022-09-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwaresModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('softwarename', models.CharField(max_length=200)),
                ('softwarecreator', models.CharField(max_length=200)),
                ('cr', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='schoolModel',
            new_name='SchoolsModel',
        ),
    ]
