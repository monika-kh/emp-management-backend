# Generated by Django 4.2.1 on 2023-07-28 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='exp',
            field=models.DecimalField(decimal_places=1, max_digits=50),
        ),
    ]
