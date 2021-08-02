from hexdump import restore as hexdump_restore


def get_resp(req):
    responses = {
        'AT': '\rOK\r',
        'AT#RSEN=1,1,0,1,0': '\rOK\r',
        'AT+CPIN?': '\rOK\r',
        'AT+CMEE=2': '\rOK\r',
        'AT+cfun=1': '\rOK\r',
        'AT+COPS=1,2,"72416"': '\rOK\r',
        'AT+COPS=1,2,"72401"': '\rOK\r',
    }

    return responses.get(req, '')


def send_message(data):
    print('[MOCK] Received: {0} bytes'.format(len(data)))
    data = data.strip()
    resp = get_resp(data)
    
    if resp:
        print('[MOCK] Message Received: {0}'.format(data))
        print('[MOCK] Message Sent: {0}'.format(resp))
    else:
        print('[MOCK] CMUX Message Received: {0}'.format(data.encode('hex')))
        resp = get_resp(data.encode('hex'))
        if resp:
            print('[MOCK] CMUX Message Sent: {0}'.format(resp))
            resp = hexdump_restore(resp)

    if resp:
        error = ''
    else:
        print('[MOCK] Invalid Message')
        error = 'INVALID MESSAGE', ''

    return error, resp
