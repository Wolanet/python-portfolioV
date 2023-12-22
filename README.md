<h2>🐍 Python portfolio </h2> 
I'm learning Python from zero. My goal is to develop tools useful for the Cybersecurity field. <br />
This repo will have all the projects I've done or I've worked on, it will be updated regularly and it'll include some simple beginner projects/scripts as well. <br />
<br />

__________________
__________________


<h2> [1] ScapyScan.py </h2>

 [Scapy](https://scapy.net/) is a Python-based packet manipulation program and library. It is able to forge and decode packets in many protocols, send them on the wire, capture them, store 
 or read them using pcap files, and much more. 
 In this script we will perform a Port scan (TCP SYN scan), a DNS scan and lastly we'll use the sniff ( ) function to sniff and output sniffed packets. <br />
 This script shows just the tip of the iceberg of what you can achieve with Scapy.

<h3> 🔶 Documentation </h3>
In this script we use the <b>sr ( ) function</b> to create and send packets: sr( ) sends and receives packets without a custom ether() layer. <br />
Other functions to send packets are: <br />
- sendp( ) = sends with a custom ether() layer  <br />
- srp( ) = sends and receives at with a custom ether() layer  <br />
- sr1( ) = sends packets without custom ether() layer and waits for first answer  <br /> <br />

It's also important to note that Scapy <b>works with layers</b>. Layers are individual functions stacked together with the "/" character to create packets. <br />
Here's an example code to build a basic TCP/IP packet with "data" as the payload >>> ```packet = IP(dst="1.2.3.4") / TCP(dport=22) / "data"``` <br />
We can also view field's values like the source port: >>> ```packet.sport```, we can set the destination IP address: >>> ```packet[IP].dst = "127.0.0.1"```, and much more.
<br />

<h4> > Performing the scans and sniffing </h4>
To perform a TCP SYN scan and a DNS scan we create 2 functions, and we used pre-defined ports and a pre-defined host (google DNS server). You can modify those values as you please to scan different ports or hosts. <br />
The first function named S_scan creates and sends TCP SYN packets (by setting the TCP flag to "S"), then with a for lop it disaplys any open port found, based on the pre-defined
ports we provide. <br />
The second function performs a DNS scan by querying google.com, and sending packets to port 53 UDP (used for DNS). <br />
Lastly, we sniff some packets with the same host, showcasing more capabilities of the Scapy library.
<br /> <br />

<h2> [2] AllowIP.py </h2>
 In a given organization, access to restricted content is controlled with an allow list of ip addresses. The "allow_list.txt" file identifies these IP addresses, and a separate remove list identifies IP addresses that 
 should no longer have access to the restricted content. <br />
 I created this script to automate updating the "allow_list.txt" of IP addresses and removing the addresses that should no longer have access. Keep in mind that the txt file can have any name, 
 just change it in the code along with the path to where it's stored. I've also added a simple regex method for searching for specific patterns.

<h3> 🔷 Documentation </h3>
 The core of this script is within the <b>update_file</b> function, defined right at the beginning. <br />
 The <b>with statement</b> is used with the .open( ) function in read mode (indicated by "r") to open the allow list file. This is so that I can have access the the file in Python and then start interacting with it. 
 While you can open files without the <b>with statement</b>, it's good practice to use it as it will help manage the resources by closing the file after exiting the statement.

<h4> > Convert the string into a list, iterate through the list and update it </h4>

 In order to remove individual IP addresses from the allow list, I needed to change it's data type from string to a list. To do this I used the .split( ) method.
 By default, the .split( ) function splits the text by whitespace into list elements, but you can choose on what to base the split on if you need to perform different types of "splits". <br />
 With the list created, I used a for loop to iterate through it, with a conditional that evaluates whether or not the loop variable element was found in the ip_addresses list. 
 Then, within that conditional, I apply the .remove( ) method to the ip_addresses list so that each IP address that is in the remove_list will be removed from ip_addresses. <br />
 Lastly, I'll use another <b>with statement</b> and open( ) but this time with a write "w" function, so that I can update the original file with the list of ip addresses. <br />
 To perform the update, I use the .join( ) method to convert the ip_addresses back into a string.

<h4> > Regular expressions </h4> 

 Regular expressions (regex) are very useful for finding specific strings (like ip addresses) in e.g. a list, here as an example I'm using a regular expression (with the re.findall( ) method)
 to find all the ip addresses that start with 192.168-- and then have 6 more digits after that.
