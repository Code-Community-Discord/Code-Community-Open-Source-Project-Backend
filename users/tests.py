from django.test import TestCase
from django.db.utils import IntegrityError
from .models import User

class UserModelTest(TestCase):

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

    def test_fetch_user_by_name(self):
        guy = User.objects.get(username__exact="Guy_Fieri")
        self.assertEquals("Guy_Fieri", guy.username)

    def test_create_user(self):
        num_users = len(User.objects.all())
        User.objects.create(
            username="Bobby_Flay",
            first_name="Bobby",
            skills="Boiling, Baking, Battling",
            background="Brisk Baking",
            goals="Best Battler",
            hobbies="Bread Baking",
            availability=True
        )
        self.assertEqual(num_users + 1, len(User.objects.all()))

    def test_invalid_duplicate_username(self):
        guy = User(
            username="Guy_Fieri",
            first_name="Guy",
            skills="Flambe, Fry, Feast",
            background="Fiery Cooking",
            goals="Fastest Flambe-r",
            hobbies="Frying and Flambe-ing",
            availability=True
        )
        with self.assertRaises(Exception) as raised:
            guy.save()
        self.assertEqual(IntegrityError, type(raised.exception))