"""

# -*- coding: utf-8 -*-
Created on          29 Jan 2019 at 10:02 AM
@author:            Arvind Sachidev Chilkoor
Created using:      PyCharm
Name of Project:    Website Blocker Project

"""

"""
This python script blocks the usage a a certain specific websites from access during a specified time interval,
The program demonstrates the use time as checkpoint for restricting access to the specified websites
"""

import time
from datetime import datetime as dt


"""
The inclusion of r before the beginning of the "" (filepath) in indicates to python that this is a row string,
this way it is incase python encounters a \n, it will NOT consider it as new-line character, but as a part of
string filepath.

"""
#hosts_temp_path = "demo_trial_hosts"               # Path location of the local hosts file with python project file

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"   # Path location of the hosts file in the C drive (Windows Machines)

redirect = "127.0.0.1"                      # The redirect to host IP address

website_list = ["www.facebook.com","facebook.com","www.ndtv.com","ndtv.com"] # List of websites that needs to be blocked


while True:
    """
    The if loop compares the current date(year,month,day,hours). This loop checks with dt.now() is more than 8.00 hrs am and less 
        than 16.00 hrs which is 4 pm
    """
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:            # here r+ gives read and write permission
            host_content = file.read()                  # opens file demo_trial_hosts thru variable hosts_temp_path
            for blklist in website_list:                # FOR loop checks each website in block list
                if blklist in host_content:             # IF loop checks is blocked website is already in the demo host file
                    pass                                # if yes, it passes and moves on to next execution
                else:
                    print('\n\n')
                    file.write(redirect + "    " + blklist + '\n')      # ELSE, the blocked website is written into the demo host file

    else:
        """
        The below code snippet removes the blocked websites, after working hours and user can browse the blocked websites.
        """
        with open(hosts_path, 'r+') as dlfile:     # Opens the file and r+ again as mentioned above gives read/write permission
            host_content = dlfile.readlines()
            dlfile.seek(0)                                # Sets the cursor to beginning of the file
            for delline in host_content:

                """Here the if loop below will check for the blocked website line by line
                , if the website is found in that line, it will NOT write into the file, this is another way of deleting
                or replacing the line.
                   """

                if not any(website in delline for website in website_list):
                    dlfile.write(delline)

            dlfile.truncate()            # file.truncate() ends the process of writing, this is a method to stop the loop and end file.
        print("Fun hours...")


    time.sleep(5)   #This code here prints 1 every 5 seconds, since time.sleep is introduced, while TRUE.

