# Generated by Django 4.0.6 on 2022-08-04 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='hireDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
