from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class BlogTest(TestCase):
    
    @classmethod
    def SetUpTestData(cls):
        testuser1= User.objects.create_user(username='testuser',password='123')
        testuser1.save()

        test_post = Post.objects.create(author='testuser',title='BlogTest',body='Content for test')
        test_post.save()



    def test_blog_content(self):
        post = Post.objects.filter(id=1)
        expected_author = f'{post.author}'
        expected_title= f'{post.title}'
        excpected_body = f'{post.body}'
        self.assertEqual(expected_author, 'testuser')
        self.assertEqual(expected_title, 'BlogTest')
        self.assertEqual(excpected_body, 'Content for test')

