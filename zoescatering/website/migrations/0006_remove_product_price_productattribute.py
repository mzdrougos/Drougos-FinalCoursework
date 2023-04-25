# Generated by Django 4.2 on 2023-04-22 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.option')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.size')),
            ],
        ),
    ]
