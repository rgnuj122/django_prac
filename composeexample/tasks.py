from __future__ import absolute_import
from composeexample.celery import app
import time
@app.task
def longtime_add(x,y):
    print 'long time task begins'
    time.sleep(5)
    print 'long time task finished'
    return x + y