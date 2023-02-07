"""
Script: 
    total_packet_delay.py
Description: 
    This script will allow one to find the 
    propagation delay for a packet from source to 
    destination with a link in between.
Instructions:
    1. Have all arguments in same format
    2. Define arguments
        - 1. Packet Length/Size (Megabytes) 
        - 2. Link Distance (Kilometers)
        - 3. Speed of travel through link (Kilometers/Second)
        - 4. Transmission Rate (Megabytes/Second)
        
Analogy:
[Packet] ->  {-Router-} -----------Link------------- {-Router-}
"""
import sys


def compute_propagation_delay(distance, speed):
    return distance/speed


def compute_transmission_delay(length, transmission_rate):
    return length/transmission_rate


def main():
    # handle arguments / usage
    USAGE_STR = "Usage: python3 total_packet_delay.py packet_length link_distance link_speed transmission_rate" + \
                "\n\t Argument Specs: \n\t\t 1. Packet Length/Size (Megabytes) \n\t\t 2. Link Distance (Kilometers) \n\t\t 3. Speed of travel through link (Kilometers/Second) \n\t\t 4. Transmission Rate (Megabytes/Second)"
    num_args = len(sys.argv)
    if (num_args != 5):
        sys.exit(USAGE_STR)

    # define arguments
    length = float(sys.argv[1])
    distance = float(sys.argv[2])
    speed = float(sys.argv[3])
    transmission_rate = float(sys.argv[4])

    # compute
    propagation_delay = compute_propagation_delay(distance, speed)
    transmission_delay = compute_transmission_delay(length, transmission_rate)
    total_delay = propagation_delay + transmission_delay

    # output
    print("%.3f Seconds" % total_delay)


main()
