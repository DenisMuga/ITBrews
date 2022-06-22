from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models



# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free. 
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email,f_name,l_name, password=None):
        """Create and return a `customUser` with an email, username,first_name,last_name, and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        customUser = self.model(username=username, email=self.normalize_email(email) ,f_name=f_name,l_name=l_name)
        customUser.set_password(password)
        customUser.save()

        return customUser

    def create_superuser(self, username, email, password):
      """
      Create and return a `customUser` with superuser powers.
      Superuser powers means that this use is an admin that can do anything
      they want.
      """
      if password is None:
          raise TypeError('Superusers must have a password.')

      customUser = self.create_user(username, email, password)
      customUser.is_superuser = True
      customUser.is_staff = True
      customUser.is_verified=True
      customUser.save()

      return customUser
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    f_name = models.CharField(('First Name'), max_length=50, blank=True)
    l_name = models.CharField(('Last Name'), max_length=50, blank=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE)
    prof_pic =models.ImageField(blank=True, upload_to='media')
    bio = models.TextField(blank=True, max_length=255 ,default='please update your bio')
    
    def __str__(self):
        return self.f_name

    def save_profile(self):
        '''Add Profile to database'''
        self.save()
   