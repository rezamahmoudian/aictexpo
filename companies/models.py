from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='عنوان شرکت')
    about = models.TextField(verbose_name='درباره شرکت', blank=True, null=True)
    manager = models.CharField(max_length=200, null=True, blank=True, verbose_name="مدیرعامل شرکت")
    manager_photo = models.ImageField(upload_to="images", null=True, blank=True, verbose_name="تصویر مدیرعامل")
    slider = models.ImageField(upload_to="images", null=True, blank=True, verbose_name="بنر شرکت")
    video = models.FileField(upload_to='media/video', null=True, blank=True )
    catalog = models.FileField(upload_to='', null=True, blank=True )
    catalog_cover = models.ImageField(upload_to="images", null=True, blank=True, verbose_name="جلد کاتالوگ")
    telephone = models.CharField(max_length=200, null=True, blank=True, verbose_name="تلفن شرکت")
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name="فکس")
    website = models.CharField(max_length=200, null=True, blank=True, verbose_name="وبسایت")
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name="ایمیل")
    mobile = models.CharField(max_length=200, null=True, blank=True, verbose_name="موبایل")
    address = models.TextField(verbose_name="آدرس", null=True, blank=True)
    certificates = models.FileField(null=True, blank=True)
    show_baner = models.BooleanField(verbose_name="نمایش بنر")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="نویسنده")

