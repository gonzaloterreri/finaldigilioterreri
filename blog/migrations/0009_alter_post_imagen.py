# Generated by Django 4.0.5 on 2022-07-25 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Blog'),
        ),
    ]
