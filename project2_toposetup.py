#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from mininet.net import Containernet
from mininet.node import RemoteController,OVSSwitch
from mininet.cli import CLI
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=RemoteController)
info('*** Adding 2 controllers\n')
c0 = net.addController('c0',port=6655)
c1 = net.addController('c1',port=6653)
info('*** Adding 4 docker containers\n')
d1 = net.addDocker('d1', mac="00:00:00:00:00:01", dimage="ubuntu:trusty")
d2 = net.addDocker('d2', mac="00:00:00:00:00:02", dimage="ubuntu:trusty")
d3 = net.addDocker('d3', mac="00:00:00:00:00:03", dimage="ubuntu:trusty")
d4 = net.addDocker('d4', mac="00:00:00:00:00:04", dimage="ubuntu:trusty")
info('*** Adding 2 switches\n')
s1 = net.addSwitch('s1',cls=OVSSwitch)
#Intf('enp0s3',node=s1)
s2 = net.addSwitch('s2',cls=OVSSwitch)
info('*** Creating links\n')
net.addLink(d1, s1) #add link from switch 1 to container 1
net.addLink(d2, s1) #add link from switch 1 to container 2
net.addLink(d3, s2) #add link from switch 2 to container 3
net.addLink(d4, s2) #add link from switch 2 to container 4
net.addLink(d1, s2) #add link from switch 2 to container 1

info('*** Starting network\n')
net.start()
c0.start()
c1.start()
s1.start([c0])
s2.start([c1])

info('*** Running CLI\n')
CLI(net)

