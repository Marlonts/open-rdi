# OpenRDI

# --------------------------------

## Get TMSI

    $ cd get_tmsi
### Radio sniffer - Get TMSI

    $ git clone https://github.com/P1sec/QCSuper

    After having installed it, you can plug your rooted phone in USB and using it is as simple as:

    $ sudo python3.7 qcsuper.py --adb --pcap-dump /<path>/pcaps/test.pcap --include-ip-traffic 

    $ sudo python3.7 qcsuper.py --adb --wireshark-live


### Get Tmsi

    $ python get_tmsi.py -f data/test.pcap

### AT Command

#### at_shell

    $ sudo python at_shell
        -p          --port              Serial Port

        $ sudo python at_shell.py -p /dev/ttyACM2

#### at_server

    $ sudo python at_server
        -p          --port              Serial Port

        $ sudo python at_server.py -p /dev/ttyACM2


# --------------------------------

## Android

Com android studio da pra visualizar o log do aparelho

No celular
- ativar modo desenvolvedor
- ativar depuração por usb

No android studio
- run
    $ ./bin/studio.sh
- logCat
 ou
- View > Tool Windows > Android Profiler

# --------------------------------

### Radio sniffer - options

https://stackoverflow.com/questions/9555403/capturing-mobile-phone-traffic-on-wireshark

https://wiki.yatebts.com/index.php/Installing

https://www.ckn.io/blog/2015/11/29/gsm-sniffing-sms-traffic/
https://github.com/CellularPrivacy/Android-IMSI-Catcher-Detector

