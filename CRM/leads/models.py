from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Machine(models.Model):
    machine_id = models.CharField(primary_key=True, max_length=6, unique=True)
    machine_name = models.CharField(max_length=50)
    date_of_first_inspection = models.DateField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.machine_name
    
    def save(self, *args, **kwargs):
        if not self.machine_id:
            self.machine_id = Machine.objects.all().count() + 1
        super().save(*args, **kwargs)

class Inspection(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    date = models.DateField()
    inspector = models.ForeignKey(Agent, on_delete=models.CASCADE)
    comments = models.TextField()

    def __str__(self):
        return self.machine