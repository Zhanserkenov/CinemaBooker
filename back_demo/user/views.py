from .models import User


def get_user(request, id):
    users = User.objects.get(id)


