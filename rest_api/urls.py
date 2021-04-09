from django.urls import path
from .views import (
    api_overview_view,
    task_list_view,
    task_add_view,
    task_detail_view,
    task_update_view,
    task_delete_view,
)

app_name = 'rest_api'

urlpatterns = [
    path('', api_overview_view, name="api-overview"),
    path('task-list/', task_list_view, name="task-list"),
    path('task-create/', task_add_view, name="task-create"),
    path('task-detail/<int:id>/', task_detail_view, name="task-detail"),
    path('task-update/<int:id>/', task_update_view, name="task-update"),
    path('task-delete/<int:id>/', task_delete_view, name="task-delete"),
]
