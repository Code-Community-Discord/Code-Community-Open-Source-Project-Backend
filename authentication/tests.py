from django.test import TestCase, Client
from users.models import User
from rest_framework.authtoken.models import Token
import json

# Create your tests here.
class AuthenticationViewTest(TestCase):

    def setUp(self):
        User.objects.create(
            username="Guy_Fieri",
            first_name="Guy",
            skills="Flambe, Fry, Feast",
            background="Fiery Cooking",
            goals="Fastest Flambe-r",
            hobbies="Frying and Flambe-ing",
            availability=True
        )

        guy = User.objects.all()[0]
        guy.set_password("fieri")
        guy.save()

    def test_get_token(self):
        c = Client()
        num_users = len(User.objects.all())
        guy = User.objects.all()[0]
        user_login = {
            "username": "Guy_Fieri",
            "password": "fieri"
        }
        response = json.loads(c.post('/authenticate', user_login, 'application/json').content)
        self.assertEqual(response['token'], guy.auth_token.key)
