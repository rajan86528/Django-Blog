from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import  Post
from http import HTTPStatus
from django.urls import reverse



class DeletePostTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', body='Test content', author=self.user)

    def test_delete_post(self):
        self.client.login(username='testuser', password='testpassword')
        delete_url = reverse('delete_post', args=[self.post.pk])
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
