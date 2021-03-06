# Generated by Django 2.1.7 on 2019-03-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='measure',
            field=models.CharField(choices=[('g', 'g'), ('cup', 'cup'), ('Tbs', 'Tbs'), ('tsp', 'tsp'), (' ', ' ')], max_length=20),
        ),
    ]
