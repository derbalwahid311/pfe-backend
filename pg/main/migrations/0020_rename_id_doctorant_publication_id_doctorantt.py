# Generated by Django 4.2.1 on 2023-05-13 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_publication_titre_publication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='ID_Doctorant',
            new_name='ID_Doctorantt',
        ),
    ]
