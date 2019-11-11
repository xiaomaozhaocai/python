import time,functools

def metric(text):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            if isinstance(text, str):
                print('Begin %s %s():' % (text, fn.__name__))
            else:
                print('Begin call %s():' % fn.__name__)
            back = fn(*args, **kw)
            print('End call')
            return back
        return wrapper
    if callable(text):
        return decorator(text)
    else:
        return decorator

@metric
def fast(x,y):
    time.sleep(0.0012)
    return x+y

@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x*y*z

f = fast(11,22)
s = slow(11,22,33)
if f!=33:
    print('测试失败！')
elif s != 7986:
    print('测试失败！')

