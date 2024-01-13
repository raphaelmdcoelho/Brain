### Concepts

It address number that locates a device. An IP address consist of two parts.
* First part: `Network address`.
* Second part: `Host address`.
### IP number

It is a 32 bits number composed for 4 block with 3 numbers separated by dot.

`0000 0000 0000 0000 0000 0000 0000 0000`
`255.255.255.255`
### Subnet Mask

Defines who is the `network` and who is the `host`. A subnet mask reveals how many bits in the IP address are used for the network by masking the network portion on the IP address.

`255.255.255.255 = 0000 0000 0000 0000 0000 0000 0000 0000`

The operation to get the network from the subnet mask is using `& bitwise` operation between subnet mask and the `ip` number.

#protocols #computing