# Generated by Django 3.2.4 on 2021-07-08 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_alter_staff_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startapper',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.country'),
        ),
    ]
