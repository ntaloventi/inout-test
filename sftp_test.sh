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
OUTGOING_FILE="$(pwd)/out/hello.txt"
INCOMING_FILE="hello_out.txt"

# Remote directory on the server
REMOTE_UPLOAD_DIR="/home/ntaloventi/wslfolder/in"
REMOTE_DOWNLOAD_DIR="/home/ntaloventi/wslfolder/out"

# Remote file names
REMOTE_UPLOAD_FILE="uploaded_hello_$TIME.txt"
REMOTE_DOWNLOAD_FILE="downloaded_hello_$TIME.txt"

# SFTP commands in a heredoc
# sshpass -p "$SFTP_PASSWORD" sftp -oBatchMode=no -b - -P $SFTP_PORT $SFTP_USER@$SFTP_HOST <<EOF
sftp -oBatchMode=no -b - -P $SFTP_PORT $SFTP_USER@$SFTP_HOST >> $LOG_FILE <<EOF
    # Change to remote directory
    cd $REMOTE_UPLOAD_DIR
    # Upload a local file as new name
    put $OUTGOING_FILE $REMOTE_UPLOAD_FILE
    # Change to remote directory
    cd $REMOTE_DOWNLOAD_DIR
    LIST="$(ls -lt)"
    echo $LIST
    # Download a remote file as new name
    # get $INCOMING_FILE $REMOTE_DOWNLOAD_FILE
    # List download folder
    # pwd
    # ls -alh
    # Exit SFTP session
    bye
EOF

# Check the exit status of the last command
if [ $? -eq 0 ]; then
    echo "SFTP script executed successfully."
else
    echo "Error in SFTP script execution."
fi
