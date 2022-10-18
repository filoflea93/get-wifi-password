import os
import re

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

strSSID = 'SSID'
strBSSID = 'BSSID'
strContenutoChiave = "Contenuto chiave"

interfaces = os.popen('netsh wlan show interfaces').read()

if strSSID in interfaces:
    if strBSSID in interfaces:
        connectionName = find_between(find_between(interfaces, strSSID, strBSSID), ': ', '\n')

stringCheckPsw = 'netsh wlan show profile name="' + connectionName + '" key=clear'
connectionData = os.popen(stringCheckPsw).read()

if strContenutoChiave in connectionData:
    str = find_between(connectionData, strContenutoChiave, '\n')

last_char = str[-1]

try:
    psw = re.search(': (.+?)'+last_char, str).group(1)
    print(psw)
except AttributeError:
    pass
