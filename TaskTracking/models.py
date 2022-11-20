from tabnanny import verbose
from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class UserTasks(models.Model):

    class Meta:
        verbose_name_plural = "User Tasks Management"

    user = models.ForeignKey('Authentication.user_Account', on_delete=models.CASCADE)
    task_name = models.CharField('Task Name',max_length=255, null=False, blank=False)
    task_description = models.TextField("Task Description", null=False, blank=False)
    task_deadline = models.DateTimeField('Deadline', null=True, blank=False)

    def __str__(self) -> str:
        return str(self.user.username) + " will do " + str(self.task_name) + " before " + str(self.task_deadline)