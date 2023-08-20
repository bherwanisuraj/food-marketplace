def detectUser(user):
    if user.role == 0:
        url = 'customer-dashboard'

    elif user.role == 1:
        url = 'vendor-dashboard'

    elif user.role is None and user.is_superadmin:
        url = '/admin'

    return url