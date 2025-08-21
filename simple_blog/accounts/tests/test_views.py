from django.contrib.auth.models import User
from django.urls import reverse
from posts.models import Post
from rest_framework.test import APITestCase


class TestLogin(APITestCase):
    '''
    This will handle login testcases
    '''

    def setUp(self):
        self.test_user1 = User.objects.create_user(username='testuser1',
                                                   password='12345')
        self.client.login(username='testuser1', password='12345')
        self.post = Post.objects.create(title='пост3', body='текст',
                                        author=self.test_user1)

    def test_create_post(self):
        data = {'title': 'title', 'description': 'description', 'body': 'body',
                'author': self.test_user1}
        resp = self.client.post(reverse('posts_api:create_post'), data)
        self.assertEqual(resp.status_code, 200)

    def test_update_post(self):
        data = {
                "title": 'новый заголовок',
                "description": "description",
                "body": "body",
                "author": self.test_user1
            }
        resp = self.client.put(
            reverse('posts_api:post_detail',
                    kwargs={'slug': self.post.slug}),
            data
        )
        self.assertEqual(resp.status_code, 200)
