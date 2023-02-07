# Propagation Delay Packets

A Python script to calculate the total delay for a packet from source to destination in a network. 

## Requirements
- Python 3

## Usage

```
python3 total_packet_delay.py packet_length link_distance link_speed transmission_rate
```


### Argument Specs
- `Packet Length/Size (Megabytes)`
- `Link Distance (Kilometers)`
- `Speed of travel through link (Kilometers/Second)`
- `Transmission Rate (Megabytes/Second)`

## Description
This script will allow you to find the total delay (propagation delay + transmission delay) for a packet traveling from source to destination in a network. 

The propagation delay is calculated as the distance between the source and destination divided by the speed of travel. 

The transmission delay is calculated as the packet length divided by the transmission rate. 

The total delay is the sum of the propagation delay and the transmission delay.

## Example

```
> python3 total_packet_delay.py 1 10 2 10
> 5.100 Seconds
```

This will calculate the total delay for a packet with a size of 1 MB, traveling a distance of 10 km, at a speed of 2 km/s and a transmission rate of 10 MB/s.
