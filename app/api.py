from django.http import HttpResponse, JsonResponse, HttpRequest
from django.contrib.auth import authenticate, login as django_login
from django.views.decorators.csrf import csrf_exempt

from migrations.models import Good

from .forms import LoginForm
from .services import populate_goods


def api_response(request, param_id):
    return JsonResponse({'some': 'data', 'param_id': param_id})


@csrf_exempt
def from_response(request) -> HttpResponse:
    """
    Handle user login from a POST request and populate the goods table if login is successful.

    Args:
        request (HttpRequest): The incoming request from the client.

    Returns:
        JsonResponse: JSON response indicating the status and message of the request.
    """
    if request.method == "POST":
        form = LoginForm(request.POST)

        # Validate form data
        if form.is_valid():
            # Authenticate user
            user = authenticate(login=form.cleaned_data['login'], password=form.cleaned_data['password'])
            
            if user:
                # User exists and the password is correct
                django_login(request, user)

                # Populate goods table from data/goods.json
                populate_goods()

                return JsonResponse({"status": "success", "message": "Logged in and goods populated"})
            
    return JsonResponse({"status": "error", "message": "Doesn't exist"})
