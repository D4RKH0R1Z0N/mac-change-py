#! /usr/bin/python

import os

def change_mac(interface, mac):
  os.system("ifconfig " + interface + " down")
  os.system("ifconfig " + interface + " hw " + "ether " + mac)
  os.system("ifconfig " + interface + " up")

interface = input("Enter which Interface you want to change the MAC : ")
new_mac = input("Enter you new MAC address : ")

change_mac(interface, new_mac)
