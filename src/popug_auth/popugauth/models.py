import uuid

from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models


class Popug(AbstractUser, PermissionsMixin):
    POPUG_ROLES = (
        ('admin', 'Administrator'),
        ('accountant', 'Accountant'),
        ('manager', 'Manager'),
        ('developer', 'Developer'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Beak ID')
    role = models.TextField(choices=POPUG_ROLES, default='developer')

    def __str__(self):
        return str(self.username)
