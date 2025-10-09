from typing import Optional, Callable
from functools import wraps
from logger import logger

PROHIBITED_NAMES = ["Saruman", "Patolino"]

def check_name(fn: Callable) -> Callable:
    """Decorator that prevents the function from executing if the name is in the prohibited list."""
    @wraps(fn)
    def wrapper(name: str, *args, **kwargs):
        normalized_name = name.strip().lower()
        if normalized_name in PROHIBITED_NAMES:
            logger.warning(f"The name '{name}' is not allowed.")
            return f"Error: the name '{name}' is not allowed."
        logger.debug(f"Name '{name}' is allowed. Executing {fn.__name__}().")
        return fn(name, *args, **kwargs)
    return wrapper


@check_name
def register_user(name: str):
    """Simulates user registration."""
    logger.info(f"User '{name}' successfully registered!")
    return f"{name} registered!"


@check_name
def send_message(name: str):
    """Simulates sending a message to the user."""
    logger.info(f"Message sent to '{name}'.")
    return f"Message to {name} sent!"


def main():
    """Demonstration of decorator that validates input strings."""

    names = ["Chico Bento", "Patolino", "Gandalf", "Saruman"]

    for name in names:
        result_1 = register_user(name)
        result_2 = send_message(name)
        logger.debug(f"Registration result: {result_1}")
        logger.debug(f"Message result: {result_2}")
        logger.debug("=" * 40)


if __name__ == "__main__":
    main()
