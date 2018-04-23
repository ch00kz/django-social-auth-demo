from pprint import pprint

def create_user(strategy, details, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    USER_FIELDS = ['first_name', 'last_name', 'email']

    fields = {field: details.get(field) for field in USER_FIELDS}

    if not fields:
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }
