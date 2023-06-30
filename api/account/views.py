from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json


@csrf_exempt
@require_http_methods(['POST'])
def signup_view(request):
    content = json.loads(request.body)
    username = content.get('email')
    password = content.get('password')
    email = content.get('email')
    try:
        user = User.objects.create_user(username=username,password=password,email=email)
        login(request,user=user)
        return JsonResponse({'message':'User create successfully'})
    except Exception as e:
        return JsonResponse({'error':str(e)},status=400)

@csrf_exempt
@require_http_methods(['POST'])
def login_view(request):  
    content = json.loads(request.body)
    username = content.get('email') or content.get('username')
    password = content.get('password') 
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return JsonResponse({'message': 'Login successful!'})
    else:
        return JsonResponse({'error': 'Invalid username or password'}, status=401)

@csrf_exempt
@require_http_methods(['GET'])
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'message':'Logged out successfully!'})
    else:
        return JsonResponse({'error':'User is not logged in!'})