# Generated by Django 4.2.1 on 2023-05-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctorant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, null=True)),
                ('prenom', models.CharField(max_length=50, null=True)),
                ('date_de_naissance', models.DateField()),
                ('lieu_de_naissance', models.CharField(help_text='dd-mm-yy', max_length=50, null=True)),
                ('adresse', models.CharField(max_length=150, null=True)),
                ('Telephone', models.IntegerField(null=True)),
                ('adresse_email', models.EmailField(max_length=254)),
                ('num_bac', models.IntegerField(null=True)),
                ('annèe_bac', models.IntegerField(null=True)),
                ('annèe_premiere_inscription', models.IntegerField(null=True)),
                ('Type', models.CharField(choices=[('lmd', 'Lmd'), ('classique', 'Classique')], max_length=10)),
            ],
        ),
    ]
