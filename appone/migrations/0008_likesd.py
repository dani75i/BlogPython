# Generated by Django 2.2.5 on 2019-09-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0007_auto_20190911_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likesd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='toto', max_length=255)),
                ('text', models.CharField(default='toto', max_length=255)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
