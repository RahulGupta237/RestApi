from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None,password2=None, mobile_number=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

     
        return user

    def create_superuser(self, email, password=None,password2=None, mobile_number=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, mobile_number, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=15,null=True,default="7084697718")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    

    
   
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Set the email field as the username field
    REQUIRED_FIELDS = ['name', 'mobile_number']  # List any other required fields

    # ... rest of your custom user model implementation ...
    def __str__(self) -> str:
        return self.email


 


class TodoList(models.Model):
    STATUS_CHOICES = (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Item(models.Model):
    item_title = models.CharField(max_length=255)
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    description = models.TextField()
    added_date = models.DateField()

    def __str__(self):
        return self.item_title
