# Generated by Django 4.2 on 2023-06-03 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_rename_id_doctorantt_journal_publication_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etablissement',
            name='Enseignant',
        ),
        migrations.AddField(
            model_name='enseignant',
            name='Etablissement',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.etablissement'),
        ),
    ]
