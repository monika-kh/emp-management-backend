# Generated by Django 4.2.1 on 2023-08-18 07:41

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_gender_employee_technologies_familiar_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(choices=[('Indore', 'Indore'), ('Bhopal', 'Bhopal'), ('Pune', 'Pune')], default='Indore', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]