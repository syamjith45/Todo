from django.urls import path
from . import views
urlpatterns = [
    path('addtask/',views.addTask,name='addtask'),
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),
    #EDIT
    path('edit/<int:pk>/',views.edit,name='edit'),
    #DELETE
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task')
]
