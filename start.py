
import nirvana
from Nirvana_Project import info

def start():
    s=info.setup_info()
    ip=s[0]
    port=s[1]
    nirvana.Nirvana.server_open(ip,port)

start()
    