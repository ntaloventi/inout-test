import os
from ftplib import FTP, error_perm

def ftp_upload(source_file, remote_path, ftp_host, ftp_user, ftp_password, port=21):
    try:
        # Connect to the FTP server
        ftp = FTP()
        ftp.connect(ftp_host, port)
        ftp.login(ftp_user, ftp_password)

        # Upload the local file
        dest_path = 'inp/test123456.txt'
        with open(source_file, 'rb') as file:
            ftp.storbinary(f"STOR {dest_path}", file)

        print(f"File uploaded successfully: {source_file} to {dest_path}")

        # Change to the desired remote directory
        try:
            ftp.cwd(remote_path)
        except error_perm as e_perm:
            print(f"Permission error: {e_perm}")
            return

        # List files in the current directory
        files = []
        ftp.retrlines('LIST', files.append)

        # Print the list of files
        print("Files in the current directory:")
        for file_info in files:
            print(file_info)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the FTP connection
        ftp.quit()

# Example usage
uploaded_path = os.getcwd() + '/out/hello.txt'
downloaded_path = '/inp'
ftp_hostname = 'ftp.iqbal.cool'
ftp_username = 'bob'
ftp_password = 'iamlove'

ftp_upload(uploaded_path, downloaded_path, ftp_hostname, ftp_username, ftp_password)
