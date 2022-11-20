from django.shortcuts import  render, redirect
from django.views.generic import ListView

from Authentication.models import user_Account
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import TaskManagementSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .forms import TaskCreationForm
from django.db.models import Q
from django.views.generic.edit import CreateView, FormView


class TaskTrackingForm(CreateView):
    form_class = TaskCreationForm
    template_name = "TaskTracking/taskcreation.html"
    success_url = "../" 


class TasksMangementApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        if request.user.is_admin:
            user_tasks = UserTasks.objects.all().values()
        else:
            user_tasks = UserTasks.objects.filter(user=request.user).values()
        content = {'user_tasks':user_tasks}
        return Response(content)
    
    def post(self, request):
        if request.user.is_admin:
            if request.POST.get('user'):
                user = request.POST.get('user')
                user = user_Account.objects.get(username=user)
            else:
                user = request.user
        else:
            user = request.user
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        task_deadline = request.POST.get('task_deadline')
        UserTasks.objects.create(
            user=user,
            task_name=task_name,
            task_description=task_description,
            task_deadline=task_deadline
        )

        content = {'message':"User's task has been updated"}
        return Response(content)
    
    def delete(self, request):
        task_name = request.POST.get('task_name')
        if request.user.is_admin:
            if request.POST.get('user'):
                user = request.POST.get('user')
                user = user_Account.objects.get(username=user)
            else:
                user = request.user
            UserTasks.objects.filter(Q(user=user)&Q(task_name=task_name)).delete()
        else:
            user = request.user
            UserTasks.objects.filter(Q(user=user)&Q(task_name=task_name)).delete()
        return Response({'message':"User's task has been updated"})
