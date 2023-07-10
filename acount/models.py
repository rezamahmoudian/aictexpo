from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="ایمیل")
    is_author = models.BooleanField(default=False, verbose_name='وضعیت نویسندگی')
    profile_img = models.ImageField(upload_to="images", default="media/images/avatar5.png", verbose_name='عکس پروفایل')
    author_request = models.BooleanField(default=False, verbose_name='درخواست نویسندگی')

    # vip_user = models.DateTimeField(default=timezone.now, verbose_name='کاربر وی آی پی تا')
    # def is_vip_user(self):
    #     if self.vip_user > timezone.now():
    #         return True
    #     else:
    #         return False
    # is_vip_user.short_description = 'کاربر ویژه'
    # is_vip_user.boolean = True

    def image_user_adminpage(self):
        return format_html("<img width=130 height=110 border-radius: 5px; src='{}'".format(self.profile_img.url))
