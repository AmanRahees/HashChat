from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,username, email, password=None):
        if not email:
            raise ValueError('Email is Required!')
        
        if not username:
            raise ValueError('Username is Required!')

        user = self.model (
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user
    

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    about = models.CharField(max_length=200, default='Available')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
    class Meta:
        verbose_name_plural = 'Users'