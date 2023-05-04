from string import ascii_letters, digits
from random import choice


def create_6_character_code(model_instance):
    """
    create 6 character code for short_code field
    """
    available_chars = ascii_letters + digits
    size = 6
    random_code = "".join([choice(available_chars) for _ in range(size)])
    model_class = model_instance.__class__
    if model_class.objects.filter(short_code=random_code).exists():
        """
        recursive function for create unique short_code
        """
        return create_6_character_code(model_instance)

    return random_code
