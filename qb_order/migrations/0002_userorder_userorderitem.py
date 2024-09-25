# Generated by Django 5.1 on 2024-09-25 06:06

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qb_order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_created_at', models.DateTimeField(auto_now_add=True)),
                ('order_updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.CharField(editable=False, max_length=150)),
                ('status', models.CharField(choices=[('IN_PROGRESS', 'IN_PROGRESS'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')], default='IN_PROGRESS', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UserOrderItem',
            fields=[
                ('user_order_item_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('item_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qb_order.fooditem')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qb_order.userorder')),
            ],
        ),
    ]
