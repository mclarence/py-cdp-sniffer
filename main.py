from scapy.all import *
import csv
load_contrib("cdp")

# get cabinet name from user 
cabinet = input("Enter cabinet name: ")

# write to csv file using csv module
with open(cabinet + ".csv", 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    while True:
        print("Waiting for CDP packet...")
        pkt = sniff(iface="Realtek PCIe GbE Family Controller", filter="ether host 01:00:0c:cc:cc:cc", count=1)
        print("Packet received!")

        switch = pkt[0]['Device ID'].val.decode("utf-8")
        port = pkt[0]['Port ID'].iface.decode("utf-8")
        vlan = pkt[0]['Native VLAN'].vlan

        print("Switch: " + switch)
        print("Port: " + port)
        print("VLAN: " + str(vlan))

        # Get patch port number from user
        patch_port = input("Enter patch port number: ")

        # write to file
        writer.writerow([cabinet, switch, port, vlan, patch_port])

        csvfile.flush()

        userInput = input("Continue? (y/n):")

        if userInput == "n":
            exit(0)





