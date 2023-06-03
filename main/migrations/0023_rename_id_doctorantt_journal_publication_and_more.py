# Generated by Django 4.2 on 2023-06-03 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_journal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='ID_Doctorantt',
            new_name='Publication',
        ),
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50, null=True)),
                ('Enseignant', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.enseignant')),
            ],
        ),
    ]