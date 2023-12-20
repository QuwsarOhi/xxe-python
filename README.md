The project contains three files:
```
attack.py  # Contians the attack code
server.py  # A server code that is vulnerable to xxe
secret     # A secret file containing secret infomraiton
```

To demonstrate the attack, run `python3 attack.py`. To manually test the server, run `python3 server.py 'xml-data'`.

The `attack.py` calls `server.py` and gives a malicious xml data to process. `server.py` processes the malicious xml (contains xxe) and echoes the xml data as output.

Upon successful attack the attacker would get the information written in `secret` file as output from `server.py`.

Note: This code only works in linux environment. It requires `lxml` python package.
