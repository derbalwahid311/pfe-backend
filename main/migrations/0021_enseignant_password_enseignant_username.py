# Generated by Django 4.2 on 2023-05-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_rename_id_doctorant_publication_id_doctorantt'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='password',
            field=models.CharField(default=0, max_length=128),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='username',
            field=models.CharField(default=0, max_length=150),
        ),
    ]