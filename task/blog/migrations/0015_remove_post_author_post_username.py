# Generated by Django 4.0.4 on 2022-06-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_rename_username_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]