# !/usr/bin/python3

import getopt, sys


def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['port='])

    if len(opt) != 1:
        print("Error: expected 1 option [-p] or [--port] ", len (opt)," received")
        sys.exit(0)

    for (op, arg) in opt:
        if (op in ['-p', '--port']):

            if int(arg) > 1000:
                port = int(arg)
            else:
                print(f'\nThe port entered is reserved, enter another port...')
                sys.exit(0)    
        else:
            print('Only the -p or --port commands are allowed')
            sys.exit(0)


    assert port is not None
    return port
