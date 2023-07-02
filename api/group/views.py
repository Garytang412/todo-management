from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from group.models import Group
import json
from .encoders import GroupListEncoder,GroupDetailEncoder



# /groups/   POST, GET
@csrf_exempt
@require_http_methods(['GET','POST'])
def group_list_view(request):

    
    if request.user.is_authenticated:
        user=request.user
        if request.method == "GET": # GET
            groups = Group.objects.filter(user=user)
            return JsonResponse({'groups':groups},encoder=GroupListEncoder,safe=False) #encoder=None, safe=False
        else: # POST
            content = json.loads(request.body)
            content['user'] = user
            new_group = Group.objects.create(**content)
            return JsonResponse(new_group,encoder=GroupDetailEncoder,safe=False)
    else:
        return JsonResponse({'error':'Unauthorized!'},status=401)
    

# /groups/<int:group_id>/ GET, PUT, DELETE
@csrf_exempt
@require_http_methods(['GET','PUT','DELETE'])
def group_detail_view(request,group_id):
    '''
    login needed:
    request.user is not None, and request.user.id == group.user_id
    1. GET:
        by group_id
        return
    2. PUT
        by group_id
        then update
        then save
        return
    3. DELETE
        find by group_id
        then delete
        return
    '''
    try:
        group = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        return JsonResponse({'error':'This group id does not exist!'},status = 404)
    
    if request.user.is_authenticated and request.user == group.user:
        user = request.user
        if request.method == 'GET':
            return JsonResponse(group,encoder=GroupDetailEncoder,safe=False)
        
        elif request.method == 'PUT':
            content = json.loads(request.body)
            group.title = content.get('title')
            group.save()
            return JsonResponse({'message':'Group updated successfully'})
        else:
            group.delete()
            return JsonResponse({'message':'Group has been deleted!'})
    else:
        return JsonResponse({'error':'Unauthorized!'},status=401)
