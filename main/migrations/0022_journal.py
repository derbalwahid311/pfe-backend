# Generated by Django 4.2 on 2023-06-03 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_enseignant_password_enseignant_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50, null=True)),
                ('Date', models.DateField(help_text='dd-mm-yy')),
                ('ID_Doctorantt', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.publication')),
            ],
        ),
    ]
