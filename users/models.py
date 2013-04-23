from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=UserManager.normalize_email(email),
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="Email address",
        max_length=255,
        unique=True,
        db_index=True,
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    #company = models.ForeignKey(Company) # TODO
    #REQUIRED_FIELDS = ('company', )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    __unicode__ = lambda self: self.email
    get_full_name = lambda self: self.email
    get_short_name = lambda self: self.email
