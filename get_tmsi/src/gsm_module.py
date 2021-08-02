# -*- coding: utf-8 -*- 

import time
import serial
import mock

from hexdump import restore as hexdump_restore


def connect(port, gsm_module_id='APP', timeout=0.1, exclusive=True):
    print(('Connecting to Serial Port: {0}, timeout: {1}'.format(port, timeout)))

    try:
        conn = serial.Serial(
            port=port,
            # baudrate=115200,
            baudrate=4000000,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            xonxoff=False,
            rtscts=False,
            dsrdtr=False,
            timeout=timeout,
            exclusive=exclusive
        )
        conn.isOpen()
        return None, conn
    except Exception as ex:
        return str(ex), None


def disconnect(conn, gsm_module_id='APP'):
    print('[{0}] Disconnecting from Serial Port: {1}'.format(gsm_module_id.upper(), conn.port))
    conn.close()


def send_message(conn, data, req_to_bytes=False, resp_to_bytes=False, is_mock=False, gsm_module_id='APP'):
    print('[{0}] Sending Message to GSM Module'.format(gsm_module_id.upper()))
    if is_mock:
        return mock.send_message(data)

    try:
        if req_to_bytes:
            data = hexdump_restore(data)

        if conn and conn.is_open:
            conn.write(data)

        time.sleep(0.1)
        if conn and not conn.is_open:
            print('[{0}] Connection closed'.format(gsm_module_id.upper()))
            return 'Connection closed', None
        else:
            # a = conn.inWaiting()
            a = conn.in_waiting
            resp = conn.read(a)

            print('[{0}] Received from GSM Module: {1} bytes'.format(gsm_module_id.upper(), len(resp)))

            if resp and resp_to_bytes:
                resp = resp.encode('hex')

            if resp:
                print('[{0}] Received Message from GSM Module: {1}'.format(gsm_module_id.upper(), resp))
            else:
                return 'Empty Response', None

            if 'ERROR' in resp:
                return resp, resp
            else:
                return None, resp

    except Exception as ex:
        print('[{0}] GSM Module Request Error:{1}'.format(gsm_module_id.upper(), ex))
        return str(ex), None


def send_at_command(conn, at, is_mock=False, gsm_module_id='APP'):
    print('[{0}] Sending AT Command to GSM Module: [at: {1}]'.format(gsm_module_id.upper(), at))
    # print(':'.join(x.encode('hex') for x in at))

    req_to_bytes = False
    resp_to_bytes = False
    message = '{0}\r'.format(at)

    error, resp = send_message(conn, message, req_to_bytes=req_to_bytes, resp_to_bytes=resp_to_bytes, is_mock=is_mock, gsm_module_id=gsm_module_id)
    if error:
        return error, None

    # _resp = resp
    resp = resp.splitlines()

    print('[{0}] Received AT Command from GSM Module: {1}'.format(gsm_module_id.upper(), resp))
    # print(':'.join(x.encode('hex') for x in _resp))

    return error, resp
