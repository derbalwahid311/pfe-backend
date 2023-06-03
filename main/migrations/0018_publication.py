# Generated by Django 4.2.1 on 2023-05-13 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_doctorant_options_alter_enseignant_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titre_Publication', models.CharField(max_length=300)),
                ('ID_Doctorant', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.doctorant')),
            ],
        ),
    ]
