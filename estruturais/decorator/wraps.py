from functools import wraps
from logger import logger

def simple_decorator(fn):
    """
    Simple decorator without functools.wraps.
    Loses metadata (name, docstring) of the original function.
    """
    def wrapper(*args, **kwargs):
        """Wrapper function (no wraps)."""
        logger.debug(f"[simple_decorator] Executing {fn.__name__}()")
        return fn(*args, **kwargs)
    return wrapper

def preserved_decorator(fn):
    """
    Decorator with functools.wraps.
    Preserves metadata (name, docstring, annotations).
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """Wrapper function (with wraps)."""
        logger.debug(f"[preserved_decorator] Executing {fn.__name__}()")
        return fn(*args, **kwargs)
    return wrapper

@simple_decorator
def greet_simple(name="unknown"):
    """Original function that says hello (no wraps)."""
    logger.info(f"Hello, {name}!")

@preserved_decorator
def greet_preserved(nome="desconhecido"):
    """Original function that says hello (with wraps)."""
    logger.info(f"Hello, {nome}!")

def main():
    """Demonstration of decorators with and without wraps."""
    logger.debug("Decorator Example")

    greet_simple("Bela")
    greet_preserved("Bela")

    logger.debug("="*40)
    logger.debug("Comparing metadata")
    logger.debug(f"greet_simple.__name__ = {greet_simple.__name__}")
    logger.debug(f"greet_simple.__doc__  = {greet_simple.__doc__}")
    logger.debug(f"greet_preserved.__name__ = {greet_preserved.__name__}")
    logger.debug(f"greet_preserved.__doc__  = {greet_preserved.__doc__}")

if __name__ == "__main__":
    main()