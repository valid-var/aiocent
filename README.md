# AIOCENT
## async fork of pycent

Async Python tools to communicate with Centrifugo HTTP API. Python >= 3.3 supported.

To install run:

```bash
pip install aiocent
```

### High-level library API

First see [available API methods in documentation](https://centrifugal.dev/docs/server/server_api#http-api).

This library contains `Client` class to send messages to Centrifugo from your python-powered backend:

```python
from aiocent import Client
import asyncio

url = "http://localhost:8000/api"
api_key = "XXX"

# initialize client instance.
client = Client(url, api_key=api_key, timeout=1)

# publish data into channel
channel = "public:chat"
data = {"input": "test"}
asyncio.run(client.publish(channel, data))

# other available methods
asyncio.run(client.unsubscribe("user_id", "channel"))
asyncio.run(client.disconnect("user_id"))
history = asyncio.run(client.history("public:chat"))
presence = asyncio.run(client.presence("public:chat"))
channels = asyncio.run(client.channels())
info = asyncio.run(client.info())
asyncio.run(client.history_remove("public:chat"))
```

`publish`, `disconnect`, `unsubscribe`, `history_remove` return `None` in case of success. Each of this commands can raise an instance of `CentException`.

I.e.:

```python
from aiocent import Client, CentException
import asyncio

client = Client("http://localhost:8000/api", api_key="XXX", timeout=1)
try:
    asyncio.run(client.publish("public:chat", {"input": "test"}))
except CentException:
    # handle exception
```

Depending on problem occurred exceptions can be:

* RequestException – HTTP request to Centrifugo failed
* ResponseError - Centrifugo returned some error on request

Both exceptions inherited from `CentException`.

### Low-level library API:

To send lots of commands in one request:

```python
from aiocent import Client, CentException
import asyncio

client = Client("http://localhost:8000/api", api_key="XXX", timeout=1)

params = {
    "channel": "python",
    "data": "hello world"
}

asyncio.run(client.add("publish", params))

try:
    result = asyncio.run(client.send())
except CentException:
    # handle exception
else:
    print(result)
```

You can use `add` method to add several messages which will be sent.

You'll get something like this in response:

```bash
[{}]
```

I.e. list of single response to each command sent. So you need to inspect response on errors (if any) yourself.

### Client initialization arguments

Required:

* address - Centrifugo HTTP API endpoint address

Optional:

* `api_key` - HTTP API key of Centrifugo 
* `timeout` (default: `1`) - timeout for HTTP requests to Centrifugo
* `json_encoder` (default: `None`) - set custom JSON encoder
* `send_func` (default: `None`) - set custom send function
* `verify` (default: `True`) - when set to `False` no certificate check will be done during requests.

## For maintainer

To release:

1. Bump version in `setup.py`
1. Changelog, push and create new tag
1. `pip install twine`
1. `pip install wheel`
1. `python setup.py sdist bdist_wheel`
1. `twine check dist/*`
1. `twine upload dist/*`
