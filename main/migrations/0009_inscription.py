# Generated by Django 4.2.1 on 2023-05-13 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_enseignant_domain_competence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Doctorant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctorant')),
            ],
        ),
    ]
