import uuid
from django.db import models
from django.contrib.auth.models import  AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from apps.users.managers import CustomUserManager


class User(AbstractUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.CharField(verbose_name=_('Username'),unique=True, max_length=300)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=300)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=300)
    email = models.EmailField(verbose_name=_('Email'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    objects = CustomUserManager()

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
