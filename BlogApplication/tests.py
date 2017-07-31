from django.test import TestCase, Client
from django.core.urlresolvers import resolve
from .views import post_list, about_text

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    # def test_about_url_resolves_to_about_view(self):
    #     found = resolve('about/')
    #     self.assertEqual(found.func, about_text)


