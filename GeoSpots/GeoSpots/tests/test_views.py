from django.test import RequestFactory, TestCase
from django.urls import reverse
from posts.models import Post, User
from posts.views import index

class IndexViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.author = User.objects.create(username='testuser')
        self.post1 = Post.objects.create(title='Test Post 1', author=self.author)
        self.post2 = Post.objects.create(title='Test Post 2', author=self.author)

    def test_index_view(self):
        request = self.factory.get(reverse('posts:index'))
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post 1')
        self.assertContains(response, 'Test Post 2')

    def test_index_view_pagination(self):
        request = self.factory.get(reverse('posts:index'), {'page': '2'})
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Test Post 1')
        self.assertContains(response, 'Test Post 2')
