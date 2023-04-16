from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **rest):
        if not email:
            raise ValueError('Email Required')

        if not password:
            raise ValueError("Password Required")

        user = self.model(
            email=self.normalize_email(email=email),
            **rest
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **rest):
        user = self.create_user(email, password, **rest)

        user.active = True
        user.admin = True
        user.staff = True

        user.save(using=self._db)
        return user

    def is_active_user(self, email):
        return self.get(email=email).is_active

    def email_exists(self, email):
        return self.filter(email=email).exists()

    def get_by_email(self, email):
        return self.get(email=email)

    def get_by_pk(self, pk):
        return self.get(pk=pk)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.BigIntegerField(unique=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)  # can login if active
    staff = models.BooleanField(default=False)  # has staff permissions
    admin = models.BooleanField(default=False)  # has admin permissiions

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    def __str__(self):
        return self.email


class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banner/')
    is_featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def get_url(self):
        return self.image.url
