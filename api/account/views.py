from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
    pass

@csrf_exempt
def login(request):
    pass