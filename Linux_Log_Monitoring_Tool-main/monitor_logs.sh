#!/bin/bash

# log file paths
AUTH_LOG="/var/log/auth.log"  # SSH and sudo logs
HISTORY_LOG="/home/$USER/.bash_history"  # command history

# SSH login attempts
echo "Recent SSH login attempts:"
grep "sshd" $AUTH_LOG | tail -n 10

# sudo usage attempts
echo -e "\nRecent sudo access attempts:"
grep "sudo" $AUTH_LOG | tail -n 10

# recent command history
echo -e "\nRecent system commands executed:"
tail -n 10 $HISTORY_LOG


