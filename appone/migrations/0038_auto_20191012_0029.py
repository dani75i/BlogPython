# Generated by Django 2.2.5 on 2019-10-11 22:29

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0037_leaveacomment_status_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveACommentInComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('status_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Dislikes_Author',
        ),
        migrations.DeleteModel(
            name='NewPost',
        ),
    ]
