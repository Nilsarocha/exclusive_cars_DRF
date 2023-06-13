# Generated by Django 3.2.19 on 2023-06-06 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrical_exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridge',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='fridge',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='fridge',
            name='width',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='television',
            name='inches',
            field=models.PositiveIntegerField(),
        ),
    ]