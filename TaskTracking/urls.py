from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


urlpatterns = [
    # path('track/',views.TaskTrackingView.as_view(), name='tracktask'),
    path('track_tasks/',views.TasksMangementApiView.as_view(), name='rest_tracktask'),
    path('create/', views.TaskTrackingForm.as_view(), name='CreateTasks'),
    # path('api-token-auth/', views.CustomAuthToken.as_view()),

]