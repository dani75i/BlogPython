# Generated by Django 2.2.5 on 2019-09-29 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0026_counts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counts',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='counts',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
