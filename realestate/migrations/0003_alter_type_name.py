# Generated by Django 4.0.5 on 2022-07-25 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0002_product_delete_producy_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(choices=[('Satılık', 'Satılık'), ('Kiralık', 'Kiralık')], default='Taşınmazın Durumunu Giriniz', max_length=10),
        ),
    ]