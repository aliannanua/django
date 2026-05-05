from access.models import Permission


def has_permission(user, resource, action):
    return Permission.objects.filter(
        role__name=user.role,
        resource__name=resource,
        action__name=action
    ).exists()