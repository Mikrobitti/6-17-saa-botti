from time import gmtime, strftime
import datetime

def get_time(reduction):
    time = datetime.datetime.utcnow() - datetime.timedelta(minutes=reduction)
    now = time.strftime( "%Y-%m-%dT%H:%M:%SZ")
    return now