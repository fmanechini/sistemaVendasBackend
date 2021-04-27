from django.core.exceptions import ValidationError

def validate_comissions(value):
    if value <= 0.00 or value >= 0.10:
        raise ValidationError(
            'the comission must be between 0 and 0.10'
        )

def greater_than_zero(value):
    if value <= 0.00:
        raise ValidationError(
            'the value must be between > 0'
        )