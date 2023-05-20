# Generated by Django 3.2.19 on 2023-05-20 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['-created_at'], 'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('R', 'Rojo'), ('A', 'Azul'), ('Am', 'Amarillo'), ('N', 'Negro'), ('M', 'Marron'), ('B', 'Blanco')], max_length=50),
        ),
    ]
