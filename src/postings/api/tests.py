from rest_framework.test import APITestCase
from rest_framework import status
from postings.models import BlogPost
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
User = get_user_model()

class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User.objects.create(username='testcfeuser', email='test@test.com')
        user_obj.set_password('somerandopassword')
        user_obj.save()

        blog_post = BlogPost.objects.create(user=user_obj,
                                           title='New Title',
                                           content='some_random_content whey')

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = BlogPost.objects.count()
        self.assertEqual(post_count, 1)

    def test_get_list(self):
        data = {}
        url = api_reverse('api-postings:post-listcreate') 
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)

    def test_post_item(self):
        data = {'title': 'some rando title', 'content': 'some more content'}
        url = api_reverse('api-postings:post-listcreate') 
        response = self.client.post(url, data, format='json')
        # should be 401 because unauthourized users cannot post blog
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
