# Generated by Django 2.0.7 on 2018-07-21 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_topic_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='Image',
            field=models.ImageField(blank=True, max_length=45, upload_to='uploads/homepage_topics/'),
        ),
    ]