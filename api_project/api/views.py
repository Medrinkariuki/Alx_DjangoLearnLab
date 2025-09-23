from django.http import HttpResponse, JsonResponse

# Homepage view
def home(request):
    return HttpResponse("Welcome to API Project!")

# Sample API endpoint
def sample_api(request):
    data = {
        "message": "This is a sample API response",
        "status": "success"
    }
    return JsonResponse(data)