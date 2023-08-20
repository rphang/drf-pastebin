from django.db import IntegrityError
from django.test import TestCase

from .models import Paste
# Create your tests here.

class PasteTestCase(TestCase):
    def setUp(self):
        Paste.objects.create(title="test", content="test content", password="test")

    def test_paste_read(self):
        paste = Paste.objects.get(title="test")
        self.assertEqual(paste.content, "test content")
        self.assertEqual(paste.slug, "test")
    
    def test_paste_password_is_valid(self):
        paste = Paste.objects.get(title="test")
        self.assertNotEqual(paste.password, "test")
        self.assertTrue(paste.check_password("test"))

    def test_paste_create(self):
        paste = Paste.objects.create(title="teste2", content="test content2", password="teste2")
        self.assertEqual(paste.content, "test content2")
        self.assertEqual(paste.slug, "teste2")
        self.assertNotEqual(paste.password, "teste2")

    def test_paste_delete(self):
        paste = Paste.objects.get(title="test")
        paste.delete()
        self.assertEqual(Paste.objects.all().count(), 0)

    def test_paste_update(self):
        paste = Paste.objects.get(title="test")
        paste.title = "test2"
        paste.content = "test content2"
        paste.syntax = "python"
        paste.password = "test2"
        paste.save()
        self.assertEqual(paste.content, "test content2")
        self.assertEqual(paste.slug, "test2")
        self.assertEqual(paste.syntax, "python")
        self.assertNotEqual(paste.password, "test2")
        self.assertEqual(Paste.objects.all().count(), 1)

    def test_fail_slug(self):
        self.assertRaises(IntegrityError, Paste.objects.create, **{"title":"test", "content":"test content"})

    def test_fail_empty_title(self):
        self.assertRaises(ValueError, Paste.objects.create, **{"title":"", "content":"test content"})

    def test_fail_empty_content(self):
        self.assertRaises(ValueError, Paste.objects.create, **{"title":"test", "content":""})