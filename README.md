<h2>🐍 Python portfolio </h2> 
I'm learning Python from zero. My goal is to develop tools useful for the Cybersecurity field. <br />
This repo will have all the projects I've done or I've worked on, it will be updated regularly and it'll include some simple beginner projects/scripts as well. <br />
<br />

__________________

<br />

<h2> [1] AllowIP.py </h2>
 In a given organization, access to restricted content is controlled with an allow list of ip addresses. The "allow_list.txt" file identifies these IP addresses, and a separate remove list identifies IP addresses that 
 should no longer have access to the restricted content. <br />
 I created this script to automate updating the "allow_list.txt" of IP addresses and removing the addresses that should no longer have access. Keep in mind that the file can have any name, just change it in the code along with the path to where
 it's stored.

<h3> 🔷 Documentation </h3>
 The <b>with statement</b> is used with the .open() function in read mode (indicated by "r") to open the allow list file. This is so that I can have access the the file in Python and then start interacting with it. 
 While you can open files without the <b>with statement</b>, it's good practice to use it as it will help manage the resources by closing the file after exiting the statement.

<h4> Convert the string into a list, iterate through the list </h4>
 In order to remove individual IP addresses from the allow list, I needed to change it's data type from string to a list. To do this I used the .split() method.
 By default, the .split() function splits the text by whitespace into list elements, but you can choose on what to base the split on if you need to perform different types of "splits". <br />
 With the list created, I used a for loop to iterate through it, with a conditional that evaluates whether or not the loop variable element was found in the ip_addresses list. 
 Then, within that conditional, I apply the .remove() method to the ip_addresses list so that each IP address that is in the remove_list will be removed from ip_addresses.

<h4> Update the file with the revised list </h4> 
   Lastly, I'll use another <b>with statement</b> and open() but this time with a write "w" function, so that I can update the original file with the list of ip addresses. <br />
   To perform the update, I use the .join() method to convert the ip_addresses back into a string.

