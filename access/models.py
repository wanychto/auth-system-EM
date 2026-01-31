from django.db import models
from users.models import User

class Roles(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

class User_role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.PROTECT)

class Business_elements(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL)

class Access_rules(models.Model):
    id = models.CharField(max_length=128, unique=True)
    role = models.ForeignKey(Roles, on_delete=models.DO_NOTHING)
    element_id = models.ForeignKey(Business_elements, on_delete=models.CASCADE)
    read_permission = models.BooleanField()
    read_all_permission = models.BooleanField()
    create_permission = models.BooleanField()
    update_permission = models.BooleanField()
    update_all_permission = models.BooleanField()
    delete_permission = models.BooleanField()
    delete_all_permission = models.BooleanField()

