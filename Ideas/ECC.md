### Setting up a virtual GPU server on ECC

Setting up a virtual GPU server using ECC was surprisingly easy. 

You can deploy it in the GUI on the ICE website and once that's done you download an SSH key which you use to connect to the server. The following command is used to connect:

```ssh -i private-ssh-key.pem -p [ssh_port] [username]@[ssh_ip]```

The `ssh-port` and `ssh_ip` can both be found in the GUI on RISE. The username was in my case `ubuntu` and the `private-ssh-key` file is the one downloaded from the security tab.

Installing nvidia drivers is also quite easy. The instructions can be found [here](https://pages.ice.ri.se/ice/documentation/ecc/gpu-servers/).

One thing to note is that ECC works in a way where you pay for the time that you have the hardware reserved. So if you have created a server and it is turned off, you will still be charged by the hour. Pricing depends on the specs of the hardware, the dummy server I set up cost about 2.9 kr/hr.

