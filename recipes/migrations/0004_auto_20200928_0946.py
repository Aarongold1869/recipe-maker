# Generated by Django 2.2 on 2020-09-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.CharField(max_length=100),
        ),
    ]