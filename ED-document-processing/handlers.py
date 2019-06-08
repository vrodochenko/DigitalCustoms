import functools


def request_exception_handler(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as ex:
            message = "Error while processing request: {}".format(ex)
            return message, 400, {'ContentType': 'text/html'}

    return wrapper
