import os
import logging
from datetime import datetime
from ftplib import FTP, error_perm

# Configure logging
logging.basicConfig(
    filename='audit.log',
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def ftp_upload(remote_upload, remote_download, source_upload, dest_download, ftp_host, ftp_user, ftp_password, port=21):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    try:
        # Connect to the FTP server
        ftp = FTP()
        ftp.connect(ftp_host, port)
        ftp.login(ftp_user, ftp_password)

        logging.info("ftp connected")

        # List all files in source folder
        filesSources = os.listdir(source_upload)

        # Print the list of files
        for fileSc in filesSources:
            # up_path = remote_upload + '/' + timestamp + '_' + fileSc
            up_path = remote_upload + '/' + fileSc 
            with open(source_upload + '/' + fileSc, 'rb') as uploadFile:
                ftp.storbinary(f"STOR {up_path}", uploadFile)

            logging.info('upload file: ' + up_path)

        # Change to the download remote directory
        ftp.cwd(remote_download)
        
        # List files in the remote directory
        files = ftp.nlst()

        # Download each file
        for filename in files:
            local_file_path = f"{dest_download}/{filename}"
            remote_file_path = f"{remote_download}/{filename}"
            with open(local_file_path, 'wb') as local_file:
                ftp.retrbinary(f"RETR {remote_file_path}", local_file.write)

            logging.info('download file: ' + filename)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the FTP connection
        ftp.quit()

# Example usage
remote_upload = '/input'
remote_download = '/output'
source_upload = os.getcwd() + '/source_out'
dest_download = os.getcwd() + '/dest_in'

ftp_hostname = 'ftp.iqbal.cool'
ftp_username = 'iqbal'
ftp_password = 'iamlove'

ftp_upload(remote_upload, remote_download, source_upload, dest_download, ftp_hostname, ftp_username, ftp_password)
