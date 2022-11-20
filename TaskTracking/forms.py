from django import forms
from . import models
# creating a form
class TaskCreationForm(forms.ModelForm):

    class Meta:
        model = models.UserTasks
        fields = "__all__"
