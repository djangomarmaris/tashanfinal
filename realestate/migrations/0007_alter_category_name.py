# Generated by Django 4.0.5 on 2022-07-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0006_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Konut', 'Konut'), ('İş Yeri', 'İş Yeri'), ('Arsa', 'Arsa'), ('Turizm', 'Turizm')], max_length=10),
        ),
    ]
