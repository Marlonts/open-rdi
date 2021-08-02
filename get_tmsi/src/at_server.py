# -*- coding: utf-8 -*- 

import gsm_module
import time

from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description='Allowed options')
    parser.add_argument('-v', '--version', action='version',
                        version='at_server version 0.3.0',
                        help='display application version')
    parser.add_argument('-p', '--port', required=False, help='Serial Port')

    return parser.parse_args()

def main():
    args = parse_args()
    port = args.port or '/dev/ttyACM0'
    print('Port:', port)

    error, conn = gsm_module.connect(port, exclusive=False)
    if error:
        print('Error:', error)
        return

    while 1:
        try:
            while 1:
                time.sleep(1)
                # a = conn.inWaiting()
                # resp = conn.read(a)
                resp = conn.read(2048)

                if resp:
                    print(resp)

        except Exception as ex:
            print('Error:', str(ex))
      
if __name__ == "__main__":
    main()
