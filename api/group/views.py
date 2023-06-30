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

    user = request.user
    user_id = user.id
    if user is not None:
        if request.method == "GET": # GET
            groups = Group.objects.filter(user=user)
            return JsonResponse({'groups':groups},encoder=GroupListEncoder,safe=False) #encoder=None, safe=False
        else: # POST
            content = json.loads(request.body)
            content['user'] = user
            new_group = Group.objects.create(**content)
            return JsonResponse(new_group,encoder=GroupDetailEncoder,safe=False)
    else:
        return JsonResponse({'error':'User is not logged in!'})
    


# /groups/<int:group_id>/ GET, PUT, DELETE
def group_detail_view(request):
    '''
    login needed:
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
    pass