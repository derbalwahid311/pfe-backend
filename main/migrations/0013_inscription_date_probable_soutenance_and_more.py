# Generated by Django 4.2.1 on 2023-05-13 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_inscription_taux_avencement_inscription_titre_sujet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='Date_Probable_Soutenance',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_de_naissance',
            field=models.DateField(help_text='dd-mm-yy'),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='lieu_de_naissance',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
