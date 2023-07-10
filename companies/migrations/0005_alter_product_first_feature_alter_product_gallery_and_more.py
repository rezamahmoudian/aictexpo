# Generated by Django 4.2.3 on 2023-07-10 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_product_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='first_feature',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ویژگی اول محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gallery',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='second_feature',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ویژگی دوم محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='third_feature',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ویژگی سوم محصول'),
        ),
    ]
