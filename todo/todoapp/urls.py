from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.u_login, name='login'),
    path('task/', views.to_do, name='task'),
    path('view_task/', views.records, name='view_task'), 
    path('delete/<int:pk>/', views.DeleteTask.as_view(), name='delete'), 
    path("task/<int:pk>/", views.TaskDetail.as_view(), name="single"),
    path('task/<int:pk>/complete', views.complete_task, name='completetask'),
    path('completed/',views.completedtasks, name='complete'),
    path('uncomplete/',views.incompletetasks, name='uncomplete'),
    path("update/<int:pk>/",views.TaskUpdate.as_view(),name='update_task'),
]

