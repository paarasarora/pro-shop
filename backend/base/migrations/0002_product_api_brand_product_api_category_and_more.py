# Generated by Django 4.0.3 on 2022-03-31 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_api',
            name='brand',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product_api',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product_api',
            name='countInStock',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_api',
            name='numReviews',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_api',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product_api',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product_api',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product_api',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
