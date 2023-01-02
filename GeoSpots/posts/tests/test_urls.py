from django.test import TestCase, Client


class GeoSpotsURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_home_url_exists_at_desired_location(self):
        """Index page is available to any users"""
        response = self.guest_client.get('/')
        self.assertTemplateUsed(response, 'posts/index.html')

    def test_posts_map_url_exists_at_desired_location(self):
        """/map page is available to any users"""
        response = self.guest_client.get('/map')
        self.assertEqual(response.status_code, 200)

    def test_posts_follow_url_exists_at_desired_location(self):
        """/follow page is available to any users"""
        response = self.guest_client.get('/follow')
        self.assertEqual(response.status_code, 200)

    def test_posts_weather_url_exists_at_desired_location(self):
        """/weather page is available to any users"""
        response = self.guest_client.get('/weather')
        self.assertEqual(response.status_code, 200)

    #def test_posts_posts_id_url_exists_at_desired_location(self):
    #    """/posts/id page is available to any users"""
    #    response = self.guest_client.get('/posts/<int:post_id>/')
    #    self.assertEqual(response.status_code, 200)

    def test_posts_user_profile_url_exists_at_desired_location(self):
        """/posts/id page is available to any users"""
        response = self.guest_client.get('profile/<str:guest_client>/')
        self.assertEqual(response.status_code, 200)
