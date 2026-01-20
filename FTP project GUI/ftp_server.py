from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

def run_ftp_server():
    authorizer = DummyAuthorizer()
    
    # Add user with full access
    user = "user"
    password = "12345"
    home_dir = os.path.abspath("ftp_home")
    os.makedirs(home_dir, exist_ok=True)

    authorizer.add_user(user, password, home_dir, perm='elradfmwMT')  # Full permissions

    handler = FTPHandler
    handler.authorizer = authorizer

    # Enable logging (optional)
    handler.banner = "Welcome to your local FTP server."

    address = ("127.0.0.1", 2121)
    server = FTPServer(address, handler)

    print(f"FTP server running at {address[0]}:{address[1]}")
    server.serve_forever()

if __name__ == "__main__":
    run_ftp_server()
