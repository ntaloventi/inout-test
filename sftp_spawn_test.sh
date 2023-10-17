#!/bin/bash

TIME=$(date +"%Y%m%d_%H%M%S")

# SFTP server details
SFTP_HOST="15.0.0.11"
SFTP_USER="ntaloventi"
SFTP_PASSWORD="iamlove"
SFTP_PORT="2323"

# Log file path
LOG_FILE="sftp_log.txt"

# Local file to upload
OUTGOING_FILE="hello.txt"
INCOMING_FILE="hello_out.txt"

# Remote directory on the server
REMOTE_UPLOAD_DIR="/home/ntaloventi/wslfolder/in"
REMOTE_DOWNLOAD_DIR="/home/ntaloventi/wslfolder/out"

# Remote file names
REMOTE_UPLOAD_FILE="uploaded_hello_$TIME.txt"
REMOTE_DOWNLOAD_FILE="downloaded_hello_$TIME.txt"

# Spawn an SFTP session using expect
spawn sftp -oBatchMode=no -P $SFTP_PORT $SFTP_USER@$SFTP_HOST >> $LOG_FILE

# Expect the password prompt and send the password
expect "password:"
send "$SFTP_PASSWORD\r"

# Send SFTP commands
send "cd $REMOTE_UPLOAD_DIR\r"
send "put $OUTGOING_FILE $REMOTE_UPLOAD_FILE\r"
send "cd $REMOTE_DOWNLOAD_DIR\r"
send "get $INCOMING_FILE $REMOTE_DOWNLOAD_FILE\r"
send "bye\r"

# Wait for the process to complete
expect eof

# Check the exit status of the last command
if [ $? -eq 0 ]; then
    echo "SFTP script executed successfully."
else
    echo "Error in SFTP script execution."
fi
