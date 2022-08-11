from django.db import models
from django.contrib.auth.models import AbstractUser

# will need frontend to enforce min character limit on signup to prevent
# empty strings for username

# Possible to utilize validators on backend to validate fields, but more intuitive to 
# do so on frontend.

class User(AbstractUser):
    # Django comes with username, password, email fields,
    # and, first_name out of the box.
    # I only included the username explicitly, so that I could add the unique constraint to it
    # the other fields listed above I did not think needed to be modified.
    username = models.CharField(max_length=150, unique=True)
    # username field allows alphanumeric, _, @, ., and -
    # for reference: https://docs.djangoproject.com/en/4.0/ref/contrib/auth/
    picture = models.TextField(blank=True)
    # blank allowable in case users do not wish to upload a
    # photo immediately or at all
    skills = models.TextField(blank=True)
    # blank allowable initially and users can add/update later
    background = models.TextField(blank=True)
    # blank allowable initially and users can add/update later
    goals = models.TextField(blank=True)
    # blank allowable initially and users can add/update later
    hobbies = models.TextField(blank=True)
    # blank allowable initially and users can add/update later
    availability = models.BooleanField(default=True)
    # Will be set to True when the User model is created
    # Additionally -- Set to True when user logs in via
    # frontend and False when user logs out

    # Will have a field of auth_token inserted from Django Rest Framework (DRF)

# will need frontend to enforce min character limit on signup to prevent
# empty strings for group name and a regex checker to prevent
# nonacceptable characters

class Group(models.Model):
    name = models.CharField(max_length=128, unique=True)
    members = models.ManyToManyField(User, through='Membership', related_name="usergroups")
    info = models.TextField(blank=True)
    date_created = models.DateField(auto_now=True)
    # should have a field of events via foreignkey relationship
    # from event model
    # Should have a field of posts via foreignkey relationship
    # from post model

class Membership(models.Model):

    class Meta:
        unique_together = ['user', 'group']
        # Limits users from being able to join the same group

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_date = models.DateField(auto_now=True)
    # role = xyz permissions
    # Haven't implemented this yet, since I'm not entirely 
    # sure which direction makes the most sense