from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.validators import validate_email
from django.http import Http404
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError as e:
            raise ValueError(_('You must provide a valid email address.'))

    def create_user(self, username, first_name, last_name, email, password=None, **extra_fields):
        if not username:
            raise ValueError(_('The username cannot be blank.'))

        if not first_name:
            raise ValueError(_('The first name is required.'))

        if not last_name:
            raise ValueError(_('The last name is required.'))

        email = self.normalize_email(email)  # Normalize email address
        self.email_validator(email)        # Validate email format

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff set to True.'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser set to True.'))

        if not password:
            raise ValueError(_('Superuser must have a password.'))

        if not email:
            raise ValueError(_('Superuser must have an email address.'))

        user = self.create_user(username, first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)
        return user

