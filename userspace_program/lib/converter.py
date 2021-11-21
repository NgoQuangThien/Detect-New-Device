import socket
import ipaddress


def u64_to_mac(macint):
    if type(macint) != int:
        raise ValueError('invalid integer')
    reverse_mac = ':'.join(['{}{}'.format(a, b)
                     for a, b
                     in zip(*[iter('{:012x}'.format(macint))]*2)])
    temp = reverse_mac.split(':')
    temp.reverse()
    return ':'.join(temp)

def u32_to_ip(ipint):
    return str(ipaddress.IPv4Address(socket.htonl(ipint)))
