# Generated by Django 5.1.6 on 2025-03-01 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundraisingcampaign',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='campaign_images/'),
        ),
        migrations.AddField(
            model_name='fundraisingcampaign',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
