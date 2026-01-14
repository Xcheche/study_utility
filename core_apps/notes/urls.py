from django.urls import path
from . import views

urlpatterns = [
    # ============================================================
    # Notes CRUD URLs
    # ============================================================
    # List all notes and create a new note
    path("notes/", views.notes, name="notes"),
    # Retrieve a single note by primary key (Detail view)
    path(
        "notes/<int:pk>/",
        views.NoteDetailView.as_view(),
        name="note_detail",
    ),
    # Update an existing note
    path(
        "update/<int:pk>/",
        views.NoteUpdateView.as_view(),
        name="update",
    ),
    # Delete a note
    path(
        "delete/<int:pk>/",
        views.NoteDeleteView.as_view(),
        name="delete",
    ),
    # Search notes
    path(
        "search/",
        views.search_notes,
        name="search",
    ),
]
