# Generated by Django 3.2.4 on 2021-07-08 18:13

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContacktsProwork',
            new_name='ContactsProwork',
        ),
        migrations.RenameModel(
            old_name='SuccessProjects',
            new_name='SuccessProject',
        ),
        migrations.RenameModel(
            old_name='SuccessProjectsTranslation',
            new_name='SuccessProjectTranslation',
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='successprojecttranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'success project Translation'},
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(blank=True, max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='full name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='startapper',
            name='bio',
            field=models.TextField(default='no bio...', max_length=400, null=True),
        ),
        migrations.AlterModelTable(
            name='successprojecttranslation',
            table='basic_successproject_translation',
        ),
    ]
