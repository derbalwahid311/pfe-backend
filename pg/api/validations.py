from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def custom_validation(data):
    username = data['username'].strip()
    password = data['password'].strip()

    if not username:
        raise ValidationError('choose another username')
    
    if not password:
        raise ValidationError("choose another password")


def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('choose another username')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError("choose another password")
    return True