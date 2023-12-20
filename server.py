#  This is a echo server
#  The server recieves xml string as command line argument
#  and it echoes back the xml string as output

#  $ server.py "xml data"

from lxml import etree
import sys

#  Change the variable to false to defend xxe vulnerability
MAKE_VULNERABLE = True

#  Fatching XML from command line argument
if len(sys.argv) != 2:
    raise ValueError("The server needs xml string as argument")
xml = sys.argv[1]

#  XML parsing setting
xparse = etree.XMLParser(resolve_entities=MAKE_VULNERABLE)
data = xml.format()

#  Parsing xml
root = etree.fromstring(data, xparse)
print(etree.tostring(root))