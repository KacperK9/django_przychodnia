# Generated by Django 3.2.3 on 2021-06-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0003_alter_pacjent_idchoroba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lekarz',
            name='specjalizacja',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]