



# /groups/   POST, GET
def group_list_view(request):
    '''
    login needed : request.user 

    1. POST:
        title, user(fk)
        create 
        return

    2. GET
        list all the groups from request.user
        Group.objects.filter(user=user)
        return

    '''
    pass


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