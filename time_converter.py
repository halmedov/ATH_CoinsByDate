import time

def convert(x_time):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(str(x_time)[:10])))[:10]

