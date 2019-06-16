#!usr/bin/env python

"""
Decorator functions.
"""

from datetime import datetime, timedelta
from functools import wraps


def timeit(func=None, good=2, ok=30, good_face=u'o(￣▽￣)d',
           ok_face=u'(๑•̀ㅂ•́)و✧', bad_face=u'(ノへ￣`)'):
    """Decorator function to time the decorated functions.

    :param func: Function.
    :param good: Time upper-bound in seconds that can be considered as good.
    :param ok: Time upper-bound in seconds that can be considered as okay.
    :param good_face: This is my good face.
    :param ok_face: This is my okay face.
    :param bad_face: This is my bad face.
    :return: Decorated function.
    """
           
    # if good standard is lower than ok standard, then make good and ok the
    # same standard; the result is there are only two grades, good and bad
    good = ok if good > ok else good

    def decorator_timeit(function):

        @wraps(function)
        def wrapped_func(*args, **kwargs):
            start = datetime.now()
            ret = function(*args, **kwargs)
            elapsed = datetime.now() - start
            face = (bad_face if elapsed > timedelta(seconds=ok)
                    else good_face if elapsed <= timedelta(seconds=good)
                    else ok_face)
            print(f'{face} {function.__name__}: {elapsed}')
            return ret

        return wrapped_func

    if func:
        return decorator_timeit(func)
    else:
        return decorator_timeit


def accepts(*types, **kwtypes):
    """Decorator function to check input to the decorated function.

    Checks all inputs and returns the check log.

    :param types: Positional types.
    :param kwtypes: Keyword types, same keys as the decorated function.
    :return: None.
    :raises: Type error if anything is not right.
    """

    def decorator_accepts(func):

        @wraps(func)
        def wrapped_func(*args, **kwargs):

            log = []
            bullet = u'ヽ(#`Д´)ﾉ'

            # get args and kwargs into a dict of kwargs
            kwargs.update(zip(func.__code__.co_varnames, args))
            # get types and kwtypes into a dict of kwtypes
            kwtypes.update(zip(func.__code__.co_varnames, types))

            for key, type_ in kwtypes.items():
                if not isinstance(kwargs[key], type_):
                    log += [f'{bullet}: arg `{key}` should be {type_}.']

            if log:
                header = u'(／‵Д′)／~ ╧╧  ٩(ŏ﹏ŏ、)۶ Ｏ(≧口≦)Ｏ (`へ´≠)'
                raise TypeError('\n'.join([header] + log))

            return func(**kwargs)

        return wrapped_func

    return decorator_accepts
