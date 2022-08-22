from django.urls import path
from . import views

app_name = 'todo_app'

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('todo/mark-as-done/<int:todo_id>', views.mark_as_done, name='delete_todo'),
#     path('todo/edit/<int:todo_id>', views.update, name='edit_todo'),
# ]

# Class based views
urlpatterns = [
    path('', views.index.as_view(), name="home"),
    path('todo/show/<int:pk>', views.show.as_view(), name="details"),
    path('todo/edit/<int:pk>', views.update.as_view(), name="edit"),
    path('todo/delete/<int:pk>', views.destroy.as_view(), name="delete"),
]

