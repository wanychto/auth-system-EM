from django.db import models
from users.models import User

class Roles(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

class User_role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    class Meta:
        unique_together =("user", "role")

class Business_elements(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Access_rules(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    element = models.ForeignKey(Business_elements, on_delete=models.CASCADE)
    read_permission = models.BooleanField(default=False)
    read_all_permission = models.BooleanField(default=False)
    create_permission = models.BooleanField(default=False)
    update_permission = models.BooleanField(default=False)
    update_all_permission = models.BooleanField(default=False)
    delete_permission = models.BooleanField(default=False)
    delete_all_permission = models.BooleanField(default=False)

