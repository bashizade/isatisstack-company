from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=255,unique=True,verbose_name="شماره تلفن همراه")
    avatar = models.FileField(upload_to="user/avatar",verbose_name="پروفایل کاربری")
    linkedin_link = models.CharField(max_length=255, blank=True,null=True,verbose_name="لینک پروفایل لینکدین")
    telegram_link = models.CharField(max_length=255, blank=True,null=True,verbose_name="لینک پروفایل تلگرام")
    instagram_link = models.CharField(max_length=255, blank=True,null=True,verbose_name="لینک پروفایل اینستاگرام")
    x_link = models.CharField(max_length=255, blank=True,null=True,verbose_name="لینک پروفایل ایکس")
    bale_link = models.CharField(max_length=255, blank=True,null=True,verbose_name="لینک پروفایل بله")
    eitaa_link = models.CharField(max_length=255, blank=True,null=True,verbose_name="لینک پروفایل ایتا")
    skills = models.CharField(max_length=255,verbose_name="مهارت ها",blank=True,null=True)
    bio = models.TextField(verbose_name="درباره من",blank=True,null=True)
    position = models.CharField(max_length=255,verbose_name="سمت")
    national_code = models.CharField(max_length=11,verbose_name="کدملی")
    birth_day = models.DateField(verbose_name="تاریخ تولد", blank=True,null=True)
    
    is_admin = models.BooleanField(verbose_name="آیا مدیر باشد؟", default=False)
    is_admin_technical = models.BooleanField(verbose_name="آیا مدیر فنی باشد؟", default=False)
    is_admin_product = models.BooleanField(verbose_name="آیا مدیر محصول باشد؟", default=False)
    is_admin_finance = models.BooleanField(verbose_name="آیا مدیر مالی باشد؟", default=False)
    is_admin_creator = models.BooleanField(verbose_name="آیا مدیر تولیدمحتوا باشد؟", default=False)
    is_employee = models.BooleanField(verbose_name="آیا کارمند باشد؟", default=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    