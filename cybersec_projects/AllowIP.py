# importing the library to utilize regex expressions and functions
import re

# function named update_file that takes in two parameters: `import_file` and `remove_list`, this is the core of the script
def update_file(import_file, remove_list):
    
  # with statement to read in the initial contents of the file
  with open(import_file, "r") as file:
    ip_addresses = file.read()
  # use .split() method to convert ip_addresses from a string to a list
  ip_addresses = ip_addresses.split()

  # iterative statement to loop through ip_addresses, then remove them if present in the remove list
  for element in ip_addresses:

    if element in remove_list:
        ip_addresses.remove(element)

  # convert ip_addresses back to a string
  ip_addresses = " ".join(ip_addresses) 

  # with statement to rewrite the original file
  with open(import_file, "w") as file:
    file.write(ip_addresses)

ip_list = "/home/csec/allow_list.txt"   # add the full path of the txt file here

# here I'm adding the ips to remove manually, but you can also upload a file with the list of ips to remove and do the same as above to read the file
ip_todelete = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57", "192.168.69.116"]

# we call the function to perform the update of the allow list
update_file(ip_list, ip_todelete)

with open("allow_list.txt", "r") as file:
      updatedlist = file.read()

# outputting the updated list of ips, and making it into a list data type again instead of a string
print("The new updated list is:\n", updatedlist.split())

# we can also use regular expressions (regex) to find specific strings or ip addresses, in case want to select just a few
# here I'm using a regular expression to find all the ip address that start with 192.168 and then have 6 more digits
print("\nNew list after regex pattern search:\n ", re.findall("192.168.\d{3}\.\d{3}", updatedlist))
