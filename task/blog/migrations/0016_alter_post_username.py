# Generated by Django 4.0.4 on 2022-06-22 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0015_remove_post_author_post_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
