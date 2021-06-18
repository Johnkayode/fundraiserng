import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.manager import CustomUserManager

import uuid
import random


#Generate account confirmation code
def gen_confirmation_code():
    cc =  random.randrange(100000, 999999)
    
    try:
        user = CustomUser.objects.get(
            confirmation_code=cc
        )
        return gen_confirmation_code()
    except CustomUser.DoesNotExist:
        pass

    return cc
    




class CustomUser(AbstractUser):

    username = None
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(_("email address"), blank=False, unique=True)
    first_name = models.CharField(_("first name"), max_length=50, blank=False)
    last_name = models.CharField(_("last name"), max_length=50, blank=False)


    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    last_login = models.DateTimeField(_("last login"), auto_now=True)
    hide_email = models.BooleanField(default=True)
    
    is_active = models.BooleanField(default=False)
    confirmation_code = models.IntegerField(
        _("confirmation code"), default=gen_confirmation_code, null=True)
    
    
    
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

  
