# Generated by Django 2.2 on 2020-09-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ManyToManyField(blank=True, to='recipes.Category'),
        ),
    ]