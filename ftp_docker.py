import os
from ftplib import FTP, error_perm

def ftp_upload(rem_up, rem_do, sc_up, dest_do, ftp_host, ftp_user, ftp_password, port=21):
    try:

        # Connect to the FTP server
        ftp = FTP()
        ftp.connect(ftp_host, port)
        ftp.login(ftp_user, ftp_password)

        # List all files in source folder
        filesSources = os.listdir(sc_up)

        # Print the list of files
        for fileSc in filesSources:
            up_path = rem_up + '/1234_' + fileSc 
            with open(sc_up + '/' + fileSc, 'rb') as uploadFile:
                ftp.storbinary(f"STOR {up_path}", uploadFile)

        # Change to the download remote directory
        ftp.cwd(rem_do)
        
        # List files in the remote directory
        files = ftp.nlst()

        # Download each file
        for filename in files:
            local_file_path = f"{dest_do}/{filename}"
            remote_file_path = f"{rem_do}/{filename}"
            with open(local_file_path, 'wb') as local_file:
                ftp.retrbinary(f"RETR {remote_file_path}", local_file.write)

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
ftp_username = 'bob'
ftp_password = 'iamlove'

ftp_upload(remote_upload, remote_download, source_upload, dest_download, ftp_hostname, ftp_username, ftp_password)
