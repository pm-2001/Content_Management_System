# Generated by Django 4.0.4 on 2022-08-01 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_alter_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='images/user.webp', upload_to='pics/'),
        ),
    ]
