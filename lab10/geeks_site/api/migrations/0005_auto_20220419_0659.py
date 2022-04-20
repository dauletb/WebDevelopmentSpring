# Generated by Django 3.2.12 on 2022-04-19 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_dessert_dish_pizza_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessert',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='set',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]