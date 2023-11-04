from django.urls import path
from . import views


urlpatterns = [

    path('tlists', views.TlistCreate.as_view()),
    path('tlists/<int:pk>', views.TlistRetrieveUpdateDestroy.as_view()),
    path('tlists/<int:pk>/complete', views.TlistComplete.as_view()),
    path('tlists/completed', views.TlistCompletedTasks.as_view()),



]