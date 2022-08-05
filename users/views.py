from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import User
import json



# Create your views here.
# def authenticate(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
@require_http_methods(["GET", "POST"])
@csrf_exempt
def users(request):
    if request.method == "GET":
        user_list = User.objects.all()
        parsed_users = [
            {
                "id": user.id,
                "username": user.username,
                "picture": user.picture,
                "skills": user.skills,
                "background": user.background,
                "goals": user.goals,
                "hobbies": user.hobbies
            } for user in user_list]

        return JsonResponse(parsed_users, status=200, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)
        possible_fields = {
            "username": 0,
            "password": 0,
            "picture": 0,
            "skills": 0,
            "background": 0,
            "goals": 0,
            "hobbies": 0,
        }

        for field in data.keys():
            if field in possible_fields:
                possible_fields[field] += 1
            else:
                return JsonResponse({"Message": f"Invalid Field: '{field}'"}, status=404)
        
        for field, value in possible_fields.items():
            if value == 0:
                return JsonResponse({"Message": f"'{field}' field requires a value"}, status=404)
            elif value > 1:
                return JsonResponse({"Message": f"'{field}' field only accepts 1 entry"}, status=404)
        new_user = User(
            username=data["username"],
            password=data["password"],
            picture=data["picture"],
            skills=data["skills"],
            background=data["background"],
            goals=data["goals"],
            hobbies=data["hobbies"]
        )
        print(f'new_user: {new_user}')

        return JsonResponse({"Message": "User created successfully"}, status=200)