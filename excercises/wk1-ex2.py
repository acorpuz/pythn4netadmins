#!/usr/bin/env python3
# Prompt a user to enter in an IP address from standard input.
# Read the IP address in and break it up into its octets.
# Print out the octets in decimal, binary, and hex.
# Format:
#   Four columns, fifteen characters wide,
#   a header column,
#   data centered in the column.

ip_addr = input("Input a valid IP address: ")
ip_octets = ip_addr.split(".")
print('Octet1         Octet2         Octet3         Octet4')
for i in ip_octets:
    print(i + "\t")
