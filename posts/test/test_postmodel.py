from django.test import TestCase
from posts.models import Post
from http import HTTPStatus
from model_bakery import baker
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()

class PostsModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()
        self.assertEqual(posts, 0)

    def test_string_rep_of_objects(self):
        post = baker.make(Post)
        self.assertEqual(str(post), post.title)
        self.assertTrue(isinstance(post, Post))



class PostAutherTest(TestCase):
    def setUp(self):
        self.user = baker.make(User)
        self.post = Post.objects.create (
            title='Test title',
            body = 'test body',
            author = self.user
        )

    def test_auther_is_instance_of_user_model(self):
        self.assertTrue(isinstance(self.user, User))

    def test_post_belong_to_user(self):
        self.assertTrue(hasattr(self.post, 'author'))
        self.assertEqual(self.post.author, self.user)


