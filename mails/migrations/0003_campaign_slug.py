# Generated by Django 5.0.4 on 2024-04-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0002_campaign_delete_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
