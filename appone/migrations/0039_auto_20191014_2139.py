# Generated by Django 2.2.5 on 2019-10-14 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0038_auto_20191012_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('notes', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Songoa',
        ),
        migrations.DeleteModel(
            name='TestList',
        ),
    ]
