# Generated by Django 4.2.7 on 2023-11-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_rename_images_employees_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
