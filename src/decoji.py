#!usr/bin/env python


from functools import wraps
import datetime


def timeit(func=None, good=2, ok=30, good_face='╰(*°▽°*)╯',
           ok_face='(๑•̀ㅂ•́)و✧', bad_face='(ノへ￣、)'):
           
    # if good standard is lower than ok standard, then make good and ok the
    # same standard; the result is there are only two grades, good and bad
    good = ok if good > ok else good

    def decorator_timeit(function):
        @wraps(function)
        def wrapped_func(*args, **kwargs):
            start = datetime.datetime.now()
            ret = function(*args, **kwargs)
            elapsed = datetime.datetime.now() - start
            face = (bad_face if elapsed.seconds > ok
                    else good_face if elapsed.seconds <= good
            else ok_face)
            print(f'{face} {function.__name__}: {elapsed}')
            return ret

        return wrapped_func

    if func:
        return decorator_timeit(func)
    else:
        return decorator_timeit
 
