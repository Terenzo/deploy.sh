#!/bin/bash
#Run this script with sudo access
#this script will creat user accounts in linux
echo "please enter username for the account you want to create"
read username
echo "the user's name you entered is "$username
sudo useradd $username
echo "$usernaem user account created successfully"
echo "set the password for the username"
sudo passwd $username
