from rest_framework import serializers
from .models import UserTasks


class TaskManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTasks
        fields = '__all__'