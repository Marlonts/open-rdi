from json import loads as json_loads
from os import system, popen
from datetime import datetime
import argparse


def run(pcap_path):
    print('Loading packets ...')
    cmd = 'tshark -r {0} -l -n -T json'.format(pcap_path)
    # cmd = "tshark -r {0} -Y 'http' -l -n -T json".format(path)
    _packets = run_command(cmd)

    packets = to_json(_packets)
    # print('Packets: ', len(packets))
    # print('Packets: ', packets)

    tmsis = []

    for i_packet, packet in enumerate(packets):
        # print('Reading packet {0}'.format(i_packet+1))
        get_tmsi(packet, tmsis)

    print('TMSIs:', len(tmsis))


def get_tmsi(data, tmsis):
    for key, value in data.items():
        if isinstance(value, dict):
            tmsis = get_tmsi(value, tmsis)

        elif "TMSI" in key.upper():
            hex_value = str(value.replace(':', ''))
            if hex_value not in tmsis:
                int_value = int(hex_value, 16)
                print(key, 'hex:', hex_value, 'int:', int_value)
                tmsis.append(hex_value)

    return tmsis


def run_command(cmd):
    p = popen(cmd)
    s = p.read()
    p.close()
    return s
    # return system(cmd)


def load_file(path,  _to_json=False):
    with open(path) as f:
        data = f.read()
    if _to_json:
        return to_json(data)
    else:
        return data


def to_json(data):
    return json_loads(data)


def convert_time(_time):
    if _time:
        try:
            _time_int = int(_time)
            date = datetime.fromtimestamp(_time_int)
            return date
        except Exception:
            return 'null'
            # return str(_time)
    else:
        return 'null'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="GET TMSI 0.1.0")
    parser.add_argument("-f", "--file", required=True, help="Input pcap file")

    return parser.parse_args()


def main():
    args = get_args()
    run(args.file)


if __name__ == "__main__":
    main()