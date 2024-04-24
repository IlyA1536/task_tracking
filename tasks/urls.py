from django.urls import path
from tasks.views import *


urlpatterns = [
    path('tasks-list/', TasksListView.as_view(), name="tasks-list"),
    path('task/<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
    path('task-create/', TaskCreateView.as_view(), name="task-create"),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name="task-delete"),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name="task-update"),
    path('task/<int:pk>/complete/', TaskCompleteView.as_view(), name="task-complete"),
    path('comment/update/<int:pk>/', CommentUpdateView.as_view(), name="comment-update"),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name="comment-delete"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
]

app_name = "tasks"
