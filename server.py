# This is a simple echo server for demonstrating an XML External Entity (XXE) vulnerability.
# The server receives an XML string as a command-line argument and echoes back the XML string as output.
# Usage: $ python server.py "<xml data>"

#  $ server.py "xml data"

from lxml import etree
import sys

# Toggle the variable MAKE_VULNERABLE to make the server vulnerable or not to XXE attacks.
# Setting this to True makes the server vulnerable by allowing the parsing of external entities.
# In a secure setting, this should be set to False.
MAKE_VULNERABLE = True

#  Fetching XML from command line argument
if len(sys.argv) != 2:
    raise ValueError("The server needs xml string as argument")
xml = sys.argv[1]

# XML parsing settings
# 'resolve_entities' controls whether external entities within the XML are processed.
# If set to True, it can lead to XXE vulnerabilities where external entities can access local resources.
xparse = etree.XMLParser(resolve_entities=MAKE_VULNERABLE)
data = xml.format()

# Parsing XML
# The etree.fromstring method parses the XML string using the specified parser settings.
# If 'resolve_entities' is True, it can interpret and load external entities, leading to potential security issues.
root = etree.fromstring(data, xparse)

# Output the parsed XML
# This is a demonstration of how the XML is echoed back.
# In a real-world scenario, echoing back parsed XML data can lead to information disclosure if external entities are resolved.
print(etree.tostring(root))

# Security Note:
# To mitigate XXE vulnerabilities, always configure XML parsers to not resolve external entities.
# Additionally, consider using more secure XML libraries that are configured securely by default.
