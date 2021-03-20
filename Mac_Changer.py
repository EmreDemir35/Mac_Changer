import subprocess
import optparse
import re

def user_inputs():
    parse_object= optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="name of interface")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")

    return parse_object.parse_args()

def mac_change(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_mac(interface):
    control=subprocess.check_output(["ifconfig",interface])
    new_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(control))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

(user_input,arguments)=user_inputs()
mac_change(user_input.interface,user_input.mac_address)
last_mac=control_mac(str(user_input.interface))

if last_mac== user_input.mac_address:
    print("Success")
else:
    print("ERROR!!!")