from django.http import JsonResponse


def get_user_info(request):
    user = request.user
    data = {
        'id': user.pk,
        'username': user.username,
        'superuser': user.is_superuser,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
    return JsonResponse(data)
