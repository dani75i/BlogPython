# Generated by Django 2.2.5 on 2019-09-11 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0005_auto_20190909_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]