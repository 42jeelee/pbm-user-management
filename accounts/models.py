from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, nickname, name, profile, password=None):
        if not email:
            raise ValueError('must provide an email address')
        if not nickname:
            raise ValueError('must provide an nickname')
        if not name:
            raise ValueError('must provide a name')
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            name = name,
            profile = profile,
            rank = 0,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, name, profile, password=None):
        user = self.create_user(
            email,
            nickname = nickname,
            name = name,
            profile = profile,
            password = password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=50, null=False, blank=False)
    profile = models.CharField(default='', max_length=200)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'nickname', 'name']

    def __str__(self):
        return self.nickname
