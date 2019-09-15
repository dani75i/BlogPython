# Generated by Django 2.2.5 on 2019-09-15 14:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0014_newpost_likes_dislikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveAComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
