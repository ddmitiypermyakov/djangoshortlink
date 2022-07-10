'''
Converter for Short_link
'''
from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = 7
AVAIABLE_CHARS = ascii_letters + digits

def random_url(chars=AVAIABLE_CHARS):
    """
    Creates a random string
    """
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )

def create_short_url(model_instance):
    """
    Checks for similarity
    """
    random_code = random_url()
    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        # Recursion function
        return create_short_url(model_instance)

    return random_code