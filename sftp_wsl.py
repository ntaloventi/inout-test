import os
import paramiko

def listContents(path):
    try:
        # List all files in the specified folder
        files = os.listdir(path)

        # Print the list of files
        print(f"Files in {path}:")
        for file in files:
            print(file)

    except FileNotFoundError:
        print(f"Error: Folder not found - {path}")
    except PermissionError:
        print(f"Error: Permission denied to access - {path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def sftp_upload(local_path, remote_path, hostname, username, private_key_path, key_password, port=2323):
    # Create an SSH client
    ssh = paramiko.SSHClient()

    # Automatically add the server's host key (this is insecure and should be avoided in production)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the server using the private key and key password
        ssh.connect(hostname, port, username, key_filename=private_key_path, password=key_password)

        # Create an SFTP client
        sftp = ssh.open_sftp()

        try:
            # Upload the file
            sftp.put(local_path, remote_path)
            print(f"File uploaded successfully: {local_path} to {remote_path}")
        finally:
            # Close the SFTP session
            sftp.close()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SSH connection
        ssh.close()

# Example usage
# listContents(os.getcwd() + "/out")

local_file_path = os.getcwd() + "/out/hello.txt"
remote_file_path = '/home/ntaloventi/wslfolder/in/hello_out.txt'
ftp_hostname = '15.0.0.11'
ftp_username = 'ntaloventi'
private_key_path = 'C:\\Users\\ntalo\\.ssh\\id_rsa'
key_password = 'iamlove'

sftp_upload(local_file_path, remote_file_path, ftp_hostname, ftp_username, private_key_path, key_password)