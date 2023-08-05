#!/usr/bin/env python

""" Example of browsing for a service (in this case, HTTP) """

from zeroconf import *
import socket
import time

class MyListener(object):
    def __init__(self):
        self.r = Zeroconf()

    def removeService(self, zeroconf, type, name):
        print('')
        print(f"Service {name} removed")

    def addService(self, zeroconf, type, name):
        print('')
        print(f"Service {name} added")
        print(f"  Type is {type}")
        if info := self.r.getServiceInfo(type, name):
            print("  Address is %s:%d" % (socket.inet_ntoa(info.getAddress()),
                                          info.getPort()))
            print("  Weight is %d, Priority is %d" % (info.getWeight(),
                                                      info.getPriority()))
            print(f"  Server is {info.getServer()}")
            if prop := info.getProperties():
                print("  Properties are")
                for key, value in prop.items():
                    print(f"    {key}: {value}")

if __name__ == '__main__':
    print("Multicast DNS Service Discovery for Python Browser test")
    r = Zeroconf()
    print("Testing browsing for a service...")
    type = "_http._tcp.local."
    listener = MyListener()
    browser = ServiceBrowser(r, type, listener)
    time.sleep(5)
    r.close()
