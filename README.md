## CWE-611:

The project contains three files:
```
attack.py  # Contains the attack code
server.py  # A server code that is vulnerable to xxe
secret     # A secret file containing secret information
```

To demonstrate the attack, run `python3 attack.py`. To manually test the server, run `python3 server.py 'xml-data'`.

The `attack.py` calls `server.py` and gives a malicious XML data to process. `server.py` processes the malicious XML (contains XXE) and echoes the XML data as output.

Upon successful attack the attacker would get the information written in `secret` file as output from `server.py`.

## Solve:

To protect the server from xxe, the XML parser has to stop resolving the entities. It can be done by changing the `MAKE_VULNERABLE = True` variable to `False` in [`server.py`](https://github.com/QuwsarOhi/xxe-python/blob/04eaceb09127db64974f56d66161e5af9ffe5809/server.py#L11). The variable is passed to the [XML parser](https://github.com/QuwsarOhi/xxe-python/blob/04eaceb09127db64974f56d66161e5af9ffe5809/server.py#L19) with a request to stop resolving entities.


## Requirements

This code only works in linux environment and python3. It requires `lxml` python package.
