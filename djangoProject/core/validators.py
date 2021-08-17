from django.core.exceptions import ValidationError


def first_letter_validator(value):
    if value[0].islower():
        raise ValidationError('Title must start with upper case letter!')
    return value


def first_name_validator(value):
    if value[0].islower():
        raise ValidationError('First name must start with upper case letter!')
    return value


def last_name_validator(value):
    if value[0].islower():
        raise ValidationError('Last name must start with upper case letter!')
    return value


def age_validator(value):
    if value < 0:
        raise ValidationError('Age must be a positive number!')


