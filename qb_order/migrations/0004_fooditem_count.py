# Generated by Django 5.1 on 2024-09-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qb_order', '0003_remove_fooditem_item_image_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
