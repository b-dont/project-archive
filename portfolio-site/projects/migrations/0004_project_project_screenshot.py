# Generated by Django 3.2.6 on 2021-08-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_project_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_screenshot',
            field=models.ImageField(blank=True, height_field=281, upload_to='project_images', width_field=500),
        ),
    ]
