from flask import make_response
from http import HTTPStatus as http

def validator(*types):
    def inner(func):
        def new_f(*args, **kwargs):
            for t in types:
                if t not in kwargs.keys():
                    return make_response("Invalid payload", http.BAD_REQUEST)
            return func(*args, **kwargs)

        return new_f

    return inner