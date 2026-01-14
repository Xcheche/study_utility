from django.urls import path

from . import views

urlpatterns = [
    # Homework URLs
    # List and Create
    # path("homework", views.HomeworkView.as_view(), name="homework"),
    path("homework", views.homework_view, name="homework"),
    path(
        "homework/update/<int:pk>/",
        views.HomeworkUpdateView.as_view(),
        name="homework_update",
    ),  # Update
    # Delete
    path(
        "homework/delete/<int:pk>/",
        views.HomeworkDeleteView.as_view(),
        name="homework_delete",
    ),
]
