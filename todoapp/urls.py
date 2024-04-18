from django.urls import path
from . import views
app_name = 'todoapp'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('todo/', views.todoappView, name='todo'),
#     path('addTodoItem/',views.addTodoView), 
#     path('deleteTodoItem/<int:id>/', views.deleteTodoView), 
#   path('updateTodoItem/<int:id>/', views.updateTodoView),
# ]# In your app's urls.py file


urlpatterns = [
    path('', views.index, name='index'),  # Assuming this is your index view
    path('todo/', views.todoappView, name='todo'),
    path('addTodoItem/', views.addTodoView, name='add_todo_item'),
    path('deleteTodoItem/<int:id>/', views.deleteTodoView, name='delete_todo_item'),
    path('updateTodoItem/<int:id>/', views.updateTodoView, name='update_todo_item'),  # Define the URL pattern for update view
]
