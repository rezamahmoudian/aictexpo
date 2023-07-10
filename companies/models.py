from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CompanyCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته')
    slug = models.CharField(max_length=100, unique=True, verbose_name='آدرس دسته')
    status = models.BooleanField(default=True, verbose_name='نمایش دادن')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام شرکت')
    slug = models.CharField(max_length=100, unique=True, verbose_name='slug')
    about = models.TextField(verbose_name='درباره شرکت', blank=True, null=True)
    manager = models.CharField(max_length=200, null=True, blank=True, verbose_name="مدیرعامل شرکت")
    manager_photo = models.ImageField(upload_to="images", null=True, blank=True, verbose_name="تصویر مدیرعامل")
    slider = models.ImageField(upload_to="images", null=True, blank=True, verbose_name="بنر شرکت")
    logo = models.ImageField(upload_to="images", null=True, blank=True, verbose_name="لوگو شرکت")
    video = models.FileField(upload_to='media/video', null=True, blank=True )
    catalog = models.FileField(upload_to='', null=True, blank=True, verbose_name='کاتالوگ شرکت')
    catalog_cover = models.ImageField(upload_to="images", null=True, blank=True, verbose_name="جلد کاتالوگ شرکت")
    telephone = models.CharField(max_length=200, null=True, blank=True, verbose_name="تلفن شرکت")
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name="فکس")
    website = models.CharField(max_length=200, null=True, blank=True, verbose_name="وبسایت")
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name="ایمیل")
    mobile = models.CharField(max_length=200, null=True, blank=True, verbose_name="موبایل")
    address = models.TextField(verbose_name="آدرس", null=True, blank=True)
    certificates = models.FileField(null=True, blank=True)
    show_baner = models.BooleanField(verbose_name="نمایش بنر")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="نویسنده", related_name="author")
    category = models.ManyToManyField(CompanyCategory, verbose_name='دسته بندی', related_name="category")

    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت ها'

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی محصول')
    slug = models.CharField(max_length=100, unique=True, verbose_name='آدرس دسته بندی محصول')
    status = models.BooleanField(default=True, verbose_name='نمایش دادن')

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصولات'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام محصول')
    slug = models.CharField(max_length=100, unique=True, verbose_name='slug')
    model = models.CharField(max_length=200, null=True, blank=True, verbose_name='مدل محصول')
    description = models.TextField(verbose_name='توضیحات محصول', blank=True, null=True)
    short_description = models.TextField(verbose_name='توضیحات کوتاه محصول', blank=True, null=True)
    gallery = models.FileField(null=True, blank=True,)
    catalog = models.FileField(upload_to='', null=True, blank=True, verbose_name='کاتالوگ محصول')
    catalog_cover = models.ImageField(upload_to="images", null=True, blank=True, verbose_name="جلد کاتالوگ محصول")
    video = models.FileField(upload_to='media/video', null=True, blank=True)
    show_sertificates = models.BooleanField(verbose_name="نمایش گواهی نامه های شرکت")
    first_feature = models.CharField(max_length=200, null=True, blank=True, verbose_name='ویژگی اول محصول')
    second_feature = models.CharField(max_length=200, null=True, blank=True, verbose_name='ویژگی دوم محصول')
    third_feature = models.CharField(max_length=200, null=True, blank=True, verbose_name='ویژگی سوم محصول')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="نویسنده",
                               related_name="product_author")
    company = models.ForeignKey(Company, verbose_name='نام شرکت', on_delete=models.CASCADE, related_name='product_company')
    category = models.ManyToManyField(ProductCategory, null=True, blank=True, verbose_name='دسته بندی محصول', related_name="product_category")
