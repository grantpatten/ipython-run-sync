# ipython-run-sync
Automatically run returned Futures synchronously

# Installation
```
ipython
%install_ext https://raw.githubusercontent.com/grantpatten/ipython-run-sync/master/run_sync.py
%load_ext run_sync
```

# Configuration
```
# Set timeout seconds on Futures.  Defaults to 5 seconds.
%run_sync_timeout 10
```

# Example Usage
```
%load_ext run_sync
from tornado.gen import coroutine, sleep, Return

@coroutine
def async_function():
    yield sleep(2)
    raise Return("Hello World")

x = async_function()
print x  # "Hello World"
```
