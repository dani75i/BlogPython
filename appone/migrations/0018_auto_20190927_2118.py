# Generated by Django 2.2.5 on 2019-09-27 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0017_auto_20190917_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='newpost_likes_dislikes',
            name='number_comments',
            field=models.CharField(default=0, max_length=100),
        ),
    ]