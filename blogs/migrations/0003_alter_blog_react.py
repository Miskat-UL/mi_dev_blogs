# Generated by Django 3.2.7 on 2021-09-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blog_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='react',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
