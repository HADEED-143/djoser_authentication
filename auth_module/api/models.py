from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class role(models.TextChoices):
        employer = 'employer'
        laborer = 'laborer'
        contractor = 'contractor'
        admins = 'admins'

    updated_at = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=10, choices=role.choices)
    is_employer = models.BooleanField(default=False)
    is_laborer = models.BooleanField(default=False)
    is_contractor = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)
"""    
REQUIRED_FIELDS = ['email', 'password', 'role', 'phone_number', 'age', 'first_name', 'last_name']
    objects = BaseUserManager()

    def save(self, *args, **kwargs):
        if self.role == 'employer':
            self.is_employer = True
        elif self.role == 'laborer':
            self.is_laborer = True
        elif self.role == 'contractor':
            self.is_contractor = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True


class laborerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=laborer)


class laborer(User):

        laborer = laborerManager()

        class Meta:
            proxy = True

        def welcome(self):
            return "Welcome, laborer %s" % self.email

class contractorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=contractor)
class contractor(User):

            contractor = contractorManager()

            class Meta:
                proxy = True

            def welcome(self):
                return "Welcome, contractor %s" % self.email


class employerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=employer)
class employer(User):

    employer = employerManager()
    class Meta:
        proxy = True

    def welcome(self):
        return "Welcome, employer %s" % self.email


class adminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=employer)
class admins(User):

    admins = adminManager()
    class Meta:
        proxy = True

    def welcome(self):
        return "Welcome, admin %s" % self.email"""