# Generated by Django 4.2.3 on 2023-07-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_company_about_alter_company_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='آدرس دسته')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش دادن')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'شرکت', 'verbose_name_plural': 'شرکت ها'},
        ),
    ]
