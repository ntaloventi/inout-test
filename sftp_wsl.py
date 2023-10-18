import os
import logging
import paramiko
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='audit.log',
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def sftp_upload(remote_upload, remote_download, source_upload, dest_download, hostname, username, password, port=22):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    # Create an SSH client
    # paramiko.util.log_to_file('paramiko.log')
    ssh = paramiko.SSHClient()

    # Automatically add the server's host key (this is insecure and should be avoided in production)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, port, username, password)
        sftp = ssh.open_sftp()

        # List source_out folder
        fileUploads = os.listdir(source_upload)

        # uploading loop
        for fileUp in fileUploads:
            sc = os.path.join(source_upload, fileUp)
            ds = os.path.join(remote_upload, timestamp + '_' + fileUp)
            sftp.put(sc, ds)
            logging.info('upload file: ' + sc + ' as: ' + ds)

        # List PTEN_OUT folder
        filesDownloads = sftp.listdir(remote_download)

        # print 
        for fileDw in filesDownloads:
            sc = os.path.join(remote_download, fileDw)
            ds = os.path.join(dest_download, timestamp + '_' + fileDw)
            sftp.get(sc, ds)
            logging.info('download file: ' + sc + ' as: ' + ds)
        
        sftp.close()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SSH connection
        ssh.close()

# Configuration
remote_upload = '/mnt/pten/PTEN_IN'
remote_download = '/mnt/pten/PTEN_OUT'
source_upload = os.getcwd() + '/PTEN_IN'
dest_download = os.getcwd() + '/PTEN_OUT'

hostname = '192.168.5.123'
username = 'czftppten'
password = 'C#3DompetCoklat'

sftp_upload(remote_upload, remote_download, source_upload, dest_download, hostname, username, password)