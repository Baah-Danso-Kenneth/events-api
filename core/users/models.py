import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import  gettext_lazy as _

from core.users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
   pkId = models.BigAutoField(primary_key=True, editable=False)
   id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
   username=models.CharField(max_length=300)
   first_name = models.CharField(max_length=300)
   last_name = models.CharField(max_length=300)
   email = models.EmailField(unique=True)
   is_staff = models.BooleanField(default=False)
   is_active = models.BooleanField(default=True)
   date_joined = models.DateTimeField(auto_now_add=True)
   last_logged_in = models.DateTimeField(auto_now=True)

   objects = CustomUserManager()

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ["username", "first_name", "last_name"]


