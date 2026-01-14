
from django.test import TestCase
from django.urls import reverse

from .models import Note


class TestUrls(TestCase):
    def test_notes_url(self):
        """Test that the 'notes' URL resolves to the correct view."""
        response = self.client.get(reverse('notes'))
        self.assertEqual(response.status_code, 200)

    def test_note_detail_url(self):
        """Test that the 'note_detail' URL resolves to the correct view."""
        # Create a note to use in the test
        note = Note.objects.create(title="Test Note", content="Test content")
        response = self.client.get(reverse('note_detail', args=[note.pk]))
        self.assertEqual(response.status_code, 200)

    def test_note_update_url(self):
        """Test that the 'update' URL resolves to the correct view."""
        # Create a note to use in the test
        note = Note.objects.create(title="Test Note", content="Test content")
        response = self.client.get(reverse('update', args=[note.pk]))
        self.assertEqual(response.status_code, 200)

    def test_note_delete_url(self):
        """Test that the 'delete' URL resolves to the correct view."""
        # Create a note to use in the test
        note = Note.objects.create(title="Test Note", content="Test content")
        response = self.client.get(reverse('delete', args=[note.pk]))
        self.assertEqual(response.status_code, 200)

