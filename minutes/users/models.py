from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import messages

class CustomUser(AbstractUser):

    STATUS = (
        ('regular', 'regular'),
        ('moderator', 'moderator')
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=50, choices=STATUS, default='regular')
    description = models.TextField('Description', max_length=400, default='', blank=True)
    is_blocked = models.BooleanField(default=False)

    def is_user_blocked(self):
        return self.is_blocked

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.pk and self.is_blocked:
            # Если пользователь заблокирован, выкидываем его из системы
            self.is_active = False
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)
