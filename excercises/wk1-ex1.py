#!/usr/bin/env python

# Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3
# (representing three corresponding IP addresses).
# Print these three variables to standard output using a
# single print statement.
# Make your print statement compatible with both Python2 and Python3.

ip_addr1 = "192.168.10.1"
ip_addr2 = "192.168.20.1"
ip_addr3 = "192.168.30.1"

print_string = (
               "IP address 1: %s\nIP address 2: %s\nIP address 3: %s"
               % (ip_addr1, ip_addr2, ip_addr3)
               )
print(print_string)
