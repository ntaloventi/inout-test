#!/bin/bash

# FTP server details
FTP_SERVER="your_ftp_server"
FTP_USER="your_ftp_username"
FTP_PASSWORD="your_ftp_password"

# Local file to upload
LOCAL_FILE="local_file.txt"

# Remote directory on the server
REMOTE_DIR="/remote/directory"

# Log in to the FTP server and upload the file
ftp -n $FTP_SERVER <<EOF
user $FTP_USER $FTP_PASSWORD
cd $REMOTE_DIR
put $LOCAL_FILE
bye
EOF

# Check the exit status of the last command
if [ $? -eq 0 ]; then
    echo "FTP script executed successfully."
else
    echo "Error in FTP script execution."
fi
