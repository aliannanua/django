from access.models import Role, Resource, Action, Permission
def create_test_data():
    admin_role, _ = Role.objects.get_or_create(name='admin')
    user_role, _ = Role.objects.get_or_create(name='user')
    orders_resource, _ = Resource.objects.get_or_create(name='orders')
    reports_resource, _ = Resource.objects.get_or_create(name='reports')
    read_action, _ = Action.objects.get_or_create(name='read')
    update_action, _ = Action.objects.get_or_create(name='update')

    Permission.objects.get_or_create(
        role=admin_role,
        resource=orders_resource,
        action=read_action
    )
    Permission.objects.get_or_create(
        role=admin_role,
        resource=reports_resource,
        action=read_action
    )
    Permission.objects.get_or_create(
        role=admin_role,
        resource=orders_resource,
        action=update_action
    )
    Permission.objects.get_or_create(
        role=user_role,
        resource=orders_resource,
        action=read_action
    )