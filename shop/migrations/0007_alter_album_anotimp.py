# Generated by Django 4.0.3 on 2022-04-06 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_album_anotimp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='anotimp',
            field=models.CharField(choices=[('Vara', 'Vara'), ('Toamna', 'Toamna'), ('Iarna', 'Iarna'), ('Primavara', 'Primavara'), ('Altele', 'Altele')], max_length=10),
        ),
    ]
