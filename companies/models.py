from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name='عنوان شرکت')
    about = models.TextField(verbose_name='درباره شرکت')
    manager = models.CharField(max_length=200, null=True, on_delete=models.SET_NULL, verbose_name="مدیرعامل شرکت")
    manager_photo = models.ImageField(upload_to="images", verbose_name="تصویر مدیرعامل")
    slider = models.ImageField(upload_to="images", verbose_name="بنر شرکت")
    video = models.FileField(upload_to='media/video', )
    catalog = models.FileField(upload_to='', )
    catalog_cover = models.ImageField(upload_to="images", verbose_name="جلد کاتالوگ")
    telephone = models.CharField(max_length=200, verbose_name="تلفن شرکت")
    fax = models.CharField(max_length=200, verbose_name="فکس")
    website = models.CharField(max_length=200, verbose_name="وبسایت")
    email = models.EmailField(max_length=200, verbose_name="ایمیل")
    mobile = models.CharField(max_length=200, verbose_name="موبایل")
    address = models.TextField(verbose_name="موبایل")
    certificates = models.FileField()
    show_baner = models.BooleanField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='نویسنده')


