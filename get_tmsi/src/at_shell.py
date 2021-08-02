# -*- coding: utf-8 -*- 

import gsm_module
import time

from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description='Allowed options')
    parser.add_argument('-v', '--version', action='version',
                        version='at_shell version 0.2',
                        help='display application version')
    parser.add_argument('-p', '--port', required=False, help='Serial Port')

    return parser.parse_args()

def main():
    args = parse_args()
    port = args.port or '/dev/ttyACM0'
    print('port', port)

    error, conn = gsm_module.connect(port, exclusive=False)
    # conn.flush()
    if error:
        print('Error:', error)
        return

    while 1:
        at = raw_input('> ')
	    if at.upper() == 'TEST':
	        at = '{0}\nWAIT=2\n{1}\n'.format('AT+CMGS=50', '88888888888888888888888888888888888888888')
                conn.write(at)
                time.sleep(1)
            else:
                at = '{0}\r'.format(at)
                conn.write(at)
#                error, resp = gsm_module.send_at_command(conn, at)
#                print error, resp
                time.sleep(1)

if __name__ == "__main__":
    main()
