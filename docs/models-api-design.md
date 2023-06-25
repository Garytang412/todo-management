### project models and api design:

---
#### User:
##### design:
    - id
    - email
    - username = email
    - password
    - - created_at
##### api: /account/
    - POST:  signup/
    - POST:  login/
    - GET:  logout/

---
#### Group:
##### design:
    - id
    - title
    - created_at
    - user (foreign key) to User
##### api:
    - GET:  /groups/
    - POST: /groups/
    - GET:  /groups/<group_id>/
    - PUT/ PATCH: /groups/<group_id>/
    - DELETE: /groups/<group_id>/

---
#### Priority:
##### design:
    - id
    - name
    - color
    - created_at
    - user (foreign key)
##### api:
    - GET:  /priorities/
    - POST: /priorities/
    - GET:  /priorities/<priority_id>/
    - PUT/ PATCH: /priorities/<priority_id>/
    - DELETE: /priorities/<priority_id>/

---
#### List:
##### design:
    - id
    - title
    - created_at
    - priority (foreign key) to Priority
    - group (foreign key) to Group
    - user (foreign key) to User
##### api:
    - GET:  /groups/<group_id>/lists/
    - POST: /groups/<group_id>/lists/
    - GET:  /groups/<group_id>/lists/<list_id>/
    - PUT/ PATCH: /groups/<group_id>/lists/<list_id>/
    - DELETE: /groups/<group_id>/lists/<list_id>/
    - PUT : /lists/<listId>/move/<groupId> 

---
#### Task:
##### design:
    - id
    - title
    - content
    - deadline
    - completed
    - created_at
    - List (foreign key)
##### api:
    - GET:  /groups/:id/lists/:id/tasks/
    - POST: /groups/:id/lists/:id/tasks/:id/
    - GET:  /groups/:id/lists/:id/tasks/:id/
    - PUT/ PATCH: /groups/:id/lists/:id/tasks/:id/
    - DELETE: /groups/:id/lists/:id/tasks/:id/
    - PUT: /tasks/<taskId>/move/<listId> 
---

