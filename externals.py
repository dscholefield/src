import re

# define an exception for an invalid IP address object new value
class NotAnIPException(Exception):
    pass

class IPAddress:

    # helper method to ensure a string is a valid IP address
    # it needs to be four quads of 0-255 separated by dots
    @staticmethod
    def is_ip(ipaddress: str) -> bool:
        # check that the ip address is a quad of 1-3 digits repeated x4
        ip_quad_pattern = re.compile(r'^(?P<quad1>\d{1,3})\.(?P<quad2>\d{1,3})\.(?P<quad3>\d{1,3})\.(?P<quad4>\d{1,3})$')
        ip_quads = ip_quad_pattern.match(ipaddress)
        if ip_quads:
            # check each quad is in range 0-255
            if (int(ip_quads.group('quad1')) < 256 and 
                int(ip_quads.group('quad2')) < 256 and 
                int(ip_quads.group('quad3')) < 256 and 
                int(ip_quads.group('quad4')) < 256):
                return True
            else:
                return False
        else:
            print("ip address %s does not match quads")
            return False
        
    def __init__(self, ipaddress: str) -> None:
        if IPAddress.is_ip(ipaddress):
            self.address = ipaddress
        else:
            raise NotAnIPException

  
if __name__ == "__main__":
    ip1 = IPAddress("123.45.67.111")
    ip2 = IPAddress("701.1.1.5")


    