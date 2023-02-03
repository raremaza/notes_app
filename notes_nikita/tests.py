from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse
from django.test import Client

from .forms import CreateNoteForm
from .models import Category, Notes

class CategoryTest(TestCase):

    def create_category(self, title="only a test"):
        return Category.objects.create(title=title)

    def create_note(self, caption="only a test", text="only a test"):
        return Notes.objects.create(caption=caption, text=text)

    def test_category_creation(self):
        c = self.create_category()
        self.assertTrue(isinstance(c, Category))
        print(c)
        self.assertEqual(str(c), c.title)

    def test_index_view(self):
        n = self.create_note()
        url = reverse("index")
        c = Client()
        resp = c.get(url) # the same as we go to the browser and hit this url and hit enter
        #resp = self.client.get(url) # the same as we go to the browser and hit this url and hit enter
        self.assertTrue(isinstance(resp,HttpResponse))
        self.assertEqual(resp.status_code, 200)
        print(resp.context['notes'][0].caption)
        self.assertIn(n.caption, resp.content.decode())
        self.assertIn(n.text, str(resp.content))
        self.assertEqual(n.caption,resp.context['notes'][0].caption)

    def test_valid_form(self):
        w = Notes.objects.create(caption='Foo', text='Bar')
        data = {'caption': w.caption, 'text': w.text, }
        form = CreateNoteForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = Notes.objects.create(caption='', text='')
        data = {'caption': w.caption, 'text': w.text, }
        form = CreateNoteForm(data=data)
        self.assertFalse(form.is_valid())

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")

    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "<h1>My notes</h1>")
        self.assertNotContains(response, "Not on the page")

    def test_homepage(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "My notes")