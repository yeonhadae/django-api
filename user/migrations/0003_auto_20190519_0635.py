# Generated by Django 2.1.7 on 2019-05-19 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190519_0433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='isSmoker',
            new_name='is_smoker',
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
