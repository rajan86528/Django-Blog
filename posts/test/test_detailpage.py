from django.test import TestCase
from posts.models import Post
from http import HTTPStatus
from model_bakery import baker
from django.contrib.auth import get_user_model




class DetailPageTest(TestCase):
    def setUp(self):
        self.post = baker.make(Post)

    def test_detail_page_return_corrent_response(self):
        response = self.client.get(self.post.get_absolute_url())
        
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response,'posts/detail.html')

    def test_deatil_page_return_corrent_content(self):
        response = self.client.get(self.post.get_absolute_url())
        
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        # self.assertContains(response, self.post.created_at)
        # self.assertContains(response, self.post.created_at.strftime('%Y-%m-%d'))
