from django.contrib.auth.models import User
from django.test import TestCase
from posts.models import Post


class FirstCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser1',
                                 password='12345')

    def test_login(self):
        login = self.client.login(username='testuser1', password='12345')
        self.assertTrue(login)


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('foo@bar.com',
                                             first_name='Иван',
                                             last_name='Иванов')
        self.post = Post.objects.create(title='пост3', body='текст',
                                        author=self.user)

    def test_str_post(self):
        expected = 'пост3'
        result = str(self.post)
        self.assertEqual(result, expected)
