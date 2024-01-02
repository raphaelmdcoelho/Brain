### Concepts

It is a protocol.
### IP number

It is a 32 bits number composed for 4 block with 3 numbers separated by dot.

`0000 0000 0000 0000 0000 0000 0000 0000`
### Subnet Mask

Defines who is the network and who is the host.

`255.255.255.255 = 0000 0000 0000 0000 0000 0000 0000 0000`

The operation to get the network from the subnet mask is using `& bitwise` operation between subnet mask and the `ip` number.

#protocols #computing