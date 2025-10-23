from functools import wraps

def singleton(cls):
    """Singleton decorator"""
    instances = {} 

    @wraps(cls)
    def wrapper(*args, **kwargs):
        print(f"Instances: {instances}")
        if cls not in instances:
            print(f"Creating single instance of {cls.__name__}")
            instances[cls] = cls(*args, **kwargs)
        else:
            print(f"Reusing existing instance of {cls.__name__}")
        return instances[cls]

    return wrapper
