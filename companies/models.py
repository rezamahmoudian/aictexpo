from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name='عنوان شرکت')
    about = models.TextField(verbose_name='درباره شرکت')
    manager = models.CharField(max_length=200, null=True, on_delete=models.SET_NULL, verbose_name="مدیرعامل شرکت")
    manager_photo = models.ImageField(upload_to="images", verbose_name="تصویر مدیرعامل")
    slider = models.ImageField(upload_to="images", verbose_name="بنر شرکت")
    video = models.FileField(upload_to='media/video', )
    catalogue = models.FileField(upload_to='', )




