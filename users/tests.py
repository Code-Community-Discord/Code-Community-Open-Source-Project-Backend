from django.test import TestCase, Client
from django.db.utils import IntegrityError
from .models import User, Group, Membership
import json

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
        guy = User.objects.all()[0]
        guy.set_password("fieri")
        guy.save()

    def test_fetch_user_by_name(self):
        guy = User.objects.get(username__exact="Guy_Fieri")
        self.assertEquals("Guy_Fieri", guy.username)

    def test_password_hasher(self):
        guy = User.objects.get(username__exact="Guy_Fieri")
        self.assertNotEqual(guy.password, 'fieri')

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
        bobby = User.objects.all()[1]
        bobby.set_password("flay")
        bobby.save()
        self.assertEqual(num_users + 1, len(User.objects.all()))

    def test_update_user_fields(self):
        guy = User.objects.get(username__exact="Guy_Fieri")
        guy.availability = False
        guy.save()
        self.assertEqual(False, guy.availability)

    def test_delete_user(self):
        num_users = len(User.objects.all())
        guy = User.objects.get(username__exact="Guy_Fieri")
        guy.delete()
        self.assertEqual(num_users - 1, len(User.objects.all()))

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
        guy.set_password("fiery")
        with self.assertRaises(Exception) as raised:
            guy.save()
        self.assertEqual(IntegrityError, type(raised.exception))

class GroupModelTest(TestCase):

    def setUp(self):
        Group.objects.create(
            name="Hogwarts Lads",
            info="Das lads"
        )

    def test_fetch_group(self):
        hogwarts = Group.objects.get(name__exact="Hogwarts Lads")
        self.assertEqual(hogwarts.name, "Hogwarts Lads")

    def test_create_group(self):
        num_groups = len(Group.objects.all())
        Group.objects.create(
            name="Culinary Greats",
            info="Group for those that belong in the culinary pantheon"
        )
        self.assertEqual(num_groups + 1, len(Group.objects.all()))

    def test_update_group_fields(self):
        hogwarts = Group.objects.get(name__exact="Hogwarts Lads")
        hogwarts.info = "Dumbledore's Army"
        hogwarts.save()
        self.assertEqual(hogwarts.info, "Dumbledore's Army")

    def test_delete_group(self):
        num_groups = len(Group.objects.all())
        hogwarts = Group.objects.get(name__exact="Hogwarts Lads")
        hogwarts.delete()
        self.assertEqual(num_groups - 1, len(Group.objects.all()))

    def test_invalid_duplicate_group_name(self):
        hogwarts = Group(
            name="Hogwarts Lads",
            info="Shady Deatheaters"
        )
        with self.assertRaises(Exception) as raised:
            hogwarts.save()
        self.assertEqual(IntegrityError, type(raised.exception))

class MembershipModelTest(TestCase):
    
    def setUp(self):
        User.objects.create(
            username="Bobby_Flay",
            password="filet",
            first_name="Bobby",
            skills="Boiling, Baking, Battling",
            background="Brisk Baking",
            goals="Best Battler",
            hobbies="Bread Baking",
            availability=True
        )
        User.objects.create(
            username="Guy_Fieri",
            password="fiery",
            first_name="Guy",
            skills="Flambe, Fry, Feast",
            background="Fiery Cooking",
            goals="Fastest Flambe-r",
            hobbies="Frying and Flambe-ing",
            availability=True
        )
        Group.objects.create(
            name="Culinary Greats",
            info="Group for those that belong in the culinary pantheon"
        )

    def test_create_and_fetch_membership(self):
        num_memberships = len(Membership.objects.all())
        guy = User.objects.get(username__exact="Guy_Fieri")
        culinary = Group.objects.get(name__exact="Culinary Greats")
        membership = Membership(user=guy, group=culinary)
        membership.save()
        self.assertEqual(num_memberships + 1, len(Membership.objects.all()))

        self.assertEqual(Membership.objects.all()[0].user.username, guy.username)

    def test_usergroup_existence(self):
        guy = User.objects.get(username__exact="Guy_Fieri")
        num_groups_for_user = len(guy.usergroups.all())
        culinary = Group.objects.get(name__exact="Culinary Greats")
        Membership.objects.create(user=guy, group=culinary)
        self.assertEqual(num_groups_for_user + 1, len(guy.usergroups.all()))

    def test_group_member_existence(self):
        guy = User.objects.get(username__exact="Guy_Fieri")
        culinary = Group.objects.get(name__exact="Culinary Greats")
        num_group_members = len(culinary.members.all())
        Membership.objects.create(user=guy, group=culinary)
        self.assertEqual(num_group_members + 1, len(culinary.members.all()))

    def test_membership_delete(self):
        guy = User.objects.get(username__exact="Guy_Fieri")
        culinary = Group.objects.get(name__exact="Culinary Greats")
        m1 = Membership(user=guy, group=culinary)
        m1.save()
        num_memberships = len(Membership.objects.all())
        num_usergroups = len(guy.usergroups.all())
        num_members = len(culinary.members.all())
        self.assertEqual(num_usergroups, num_members)
        m1.delete()
        num_usergroups = len(guy.usergroups.all())
        num_members = len(culinary.members.all())
        self.assertEqual(num_memberships - 1, len(Membership.objects.all()))
        self.assertEqual(num_usergroups, num_members)

    def test_no_duplicate_membership_allowed(self):
        guy = User.objects.get(username__exact="Guy_Fieri")
        culinary = Group.objects.get(name__exact="Culinary Greats")
        m1 = Membership(user=guy, group=culinary)
        m1.save()
        m2 = Membership(user=guy, group=culinary)
        with self.assertRaises(Exception) as raised:
            m2.save()
        self.assertEqual(IntegrityError, type(raised.exception))

    def test_group_member_addition(self):
        guy = User.objects.get(username__exact="Guy_Fieri")
        bobby = User.objects.get(username__exact="Bobby_Flay")
        culinary = Group.objects.get(name__exact="Culinary Greats")
        num_memberships = len(culinary.members.all())
        Membership.objects.create(user=guy, group=culinary)
        Membership.objects.create(user=bobby, group=culinary)
        self.assertEqual(num_memberships + 2, len(culinary.members.all()))
    
    def test_group_delete_membership_count(self):
        guy = User.objects.get(username__exact="Guy_Fieri")
        bobby = User.objects.get(username__exact="Bobby_Flay")
        culinary = Group.objects.get(name__exact="Culinary Greats")
        Membership.objects.create(user=guy, group=culinary)
        Membership.objects.create(user=bobby, group=culinary)
        num_memberships = len(culinary.members.all())
        guy_groups = len(guy.usergroups.all())
        bobby_groups = len(bobby.usergroups.all())
        culinary.delete()
        self.assertEqual(guy_groups - 1, len(guy.usergroups.all()))
        self.assertEqual(bobby_groups - 1, len(bobby.usergroups.all()))
        self.assertEqual(num_memberships - 2, len(Membership.objects.all()))


class UserViewTest(TestCase):

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

    def test_fetch_user(self):
        c = Client()
        response = json.loads(c.get('/users/1').content)
        guy = User.objects.get(username__exact="Guy_Fieri")
        self.assertEqual(guy.username, "Guy_Fieri")

    def test_create_user(self):
        c = Client()
        new_user = {
            "username": "Bobby_Flay",
            "password": "flay",
            "first_name": "Bobby",
            "skills": "Boiling, Baking, Battling",
            "background": "Brisk Baking",
            "goals": "Best Battler",
            "hobbies": "Bread Baking",
        }
        response = c.post('/users', new_user, 'application/json').status_code
        self.assertEqual(200, response)