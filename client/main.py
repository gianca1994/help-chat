# !/usr/bin/python3

import getopt
import sys


def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:z:r:', [
        'host=', 'port=', 'zone=', 'rol='])

    if len(opt) != 4:
        print(f"""Error: expected 4 options:
- [-h] or [--host]
- [-p] or [--port] 
- [-z] or [--zone] 
- [-r] or [--rol] 
You entered: {len (opt)} options.
""")
        sys.exit(0)

    for (op, arg) in opt:
        if (op in ['-h', '--host']):
            host = str(arg)

        elif (op in ['-p', '--port']):
            port = int(arg)

        elif (op in ['-z', '--zone']):
            zone = str(arg)

        elif (op in ['-r', '--rol']):
            rol = str(arg)

        else:
            print('The option entered is not valid.')
            
    assert (host, port, zone, rol) is not None
    return host, port, zone, rol

