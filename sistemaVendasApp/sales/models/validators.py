from django.core.exceptions import ValidationError

def validate_comissions(comission):
    if comission <= 0.00 or comission >= 0.10:
        raise ValidationError(
            'the comission must be between 0 and 0.10',
            params={'comission': comission},
        )