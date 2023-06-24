from django.http import HttpResponse,JsonResponse

# Create your views here.
def testView(req):
    return JsonResponse(data={"hello":"world!"})