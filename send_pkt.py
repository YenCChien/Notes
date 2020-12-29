from winpcapy import WinPcapUtils

def send(src,dst,protocol,data):
    packet = dst+src+protocol+data.encode('hex')+'00'
    print packet
    WinPcapUtils.send_packet("*Ethernet*", packet.decode("hex"))

send('30e1718403f4','ffffffffffff','1234','info')
send('30e1718403f4','bc140141abc5','1234','info')
send('30e1718403f4','bc1401db77e5','1234','info')
send('30e1718403f4','bc1401db77e5','1234','CB\t0\trf 1 n')
send('30e1718403f4','bc1401db77e5','1234','CCU\tip 192.168.84.100 255.255.255.0 192.168.100.20 255.255.255.0')

send('30e1718403f4','bc1401db77e5','1234','CCU\tprelay 3011 vlan11 23 192.168.100.1 23')
send('30e1718403f4','bc1401db77e5','1234','CCU\tprelay 3012 vlan12 23 192.168.100.1 23')
send('30e1718403f4','bc1401db77e5','1234','CCU\tprelay 3013 vlan13 23 192.168.100.1 23')
send('30e1718403f4','bc1401db77e5','1234','CCU\tprelay 3014 vlan14 23 192.168.100.1 23')

send('30e1718403f4','bc1401db77e5','1234','CB\t0\t?')
send('30e1718403f4','bc1401db77e5','1234','CB\t0\tpwr 2')

# "434355097072656c6179203330313120766c616e3131203233203139322e3136382e3130302e3120323300".decode('hex')

from scapy.all import *

sendp(eval("Ether(src='30:e1:71:84:03:f4', dst='ff:ff:ff:ff:ff:ff', type=4660)/Raw(load='info')"))
sendp(eval("Ether(src='30:e1:71:84:03:f4', dst='bc:14:01:41:ab:c5', type=4660)/Raw(load='info')"))
sendp(eval("Ether(src='30:e1:71:84:03:f4', dst='bc:14:01:db:77:e5', type=4660)/Raw(load='info')"))
sendp(eval("Ether(src='30:e1:71:84:03:f4', dst='bc:14:01:db:77:e5', type=4660)/Raw(load='CB\t0\trf 1 n')"))
sendp(eval("Ether(src='30:e1:71:84:03:f4', dst='bc:14:01:db:77:e5', type=4660)/Raw(load='CCU\tip 192.168.84.100  255.255.255.0 192.168.100.20 255.255.255.0')"))

sendp(eval("Ether(src='30:e1:71:84:03:f4', dst='bc:14:01:db:77:e5', type=4660)/Raw(load='CCU\tprelay 3011 vlan11 23 192.168.100.1 23')"))
sendp(eval("Ether(src='30:e1:71:84:03:f4', dst='bc:14:01:db:77:e5', type=4660)/Raw(load='CCU\tprelay 3021 vlan11 23 192.168.100.1 23')"))
sendp(eval("Ether(src='30:e1:71:84:03:f4', dst='bc:14:01:db:77:e5', type=4660)/Raw(load='CCU\tprelay 3031 vlan11 23 192.168.100.1 23')"))
sendp(eval("Ether(src='30:e1:71:84:03:f4', dst='bc:14:01:db:77:e5', type=4660)/Raw(load='CCU\tprelay 3041 vlan11 23 192.168.100.1 23')"))

sendp(eval("Ether(src='30:e1:71:84:03:f4', dst='bc:14:01:db:77:e5', type=4660)/Raw(load='CB\t0\t?')"))
sendp(eval("Ether(src='30:e1:71:84:03:f4', dst='bc:14:01:db:77:e5', type=4660)/Raw(load='CB\t0\tpwr 1')"))