# Generated by Django 4.2.1 on 2023-05-13 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_inscription_date_probable_soutenance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='Date_Probable_Soutenance',
            field=models.DateField(help_text='dd-mm-yy'),
        ),
    ]
