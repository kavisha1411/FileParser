# Generated by Django 4.0 on 2022-01-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileapp', '0002_alter_bookingdata_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdata',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='phone'),
        ),
    ]
