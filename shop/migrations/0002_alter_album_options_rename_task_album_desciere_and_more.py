# Generated by Django 4.0.3 on 2022-04-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'toate postarile', 'verbose_name_plural': 'postari'},
        ),
        migrations.RenameField(
            model_name='album',
            old_name='task',
            new_name='desciere',
        ),
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(upload_to='shop_images/'),
        ),
    ]
