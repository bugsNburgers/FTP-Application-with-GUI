# FTP File Transfer Application with GUI

A Python-based FTP (File Transfer Protocol) client-server application with a graphical user interface (GUI) built using Tkinter. This project demonstrates file transfer capabilities between a local client and an FTP server with real-time progress tracking.

## 📋 Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Default Test Files](#default-test-files)
- [Screenshots](#screenshots)
- [Technical Details](#technical-details)
- [Troubleshooting](#troubleshooting)

## ✨ Features

### FTP Server
- **Local FTP Server**: Built using `pyftpdlib` library
- **User Authentication**: Secure login with username and password
- **Custom Home Directory**: Dedicated `ftp_home` folder for file storage
- **Full Permissions**: Read, write, delete, and modify file permissions
- **Port Configuration**: Runs on custom port 2121 (configurable)

### FTP Client GUI
- **Intuitive GUI**: User-friendly Tkinter-based interface
- **Easy Connection**: Simple connection setup with host, port, username, and password
- **Dual File View**: Side-by-side display of local and remote files
- **File Upload**: Upload files from local machine to FTP server
- **File Download**: Download files from FTP server to local machine
- **Progress Bar**: Real-time transfer progress visualization
- **Auto Refresh**: Update file listings after transfers
- **Binary Mode**: Supports all file types including audio, video, images, and documents

## 📁 Project Structure

```
FTP project GUI/
│
├── ftp_server.py          # FTP Server implementation
├── ftp_gui_client.py      # FTP Client with GUI
├── ftp_home/              # Server's root directory
│   ├── voice.wav          # Sample audio file
│   ├── vid.mp4            # Sample video file
│   └── ftp_server.py      # (Copy of server script)
│
├── voice.wav              # Test audio file for upload
├── vid.mp4                # Test video file for upload
├── test.txt               # Test text file
├── aa.c                   # Additional C file
├── aa.exe                 # Compiled executable
│
└── README.md              # This file
```

## 🔧 Requirements

### Python Version
- Python 3.6 or higher

### Required Libraries
```bash
pip install pyftpdlib
```

### Built-in Libraries (No installation needed)
- tkinter (usually comes with Python)
- ftplib
- os
- threading

## 📥 Installation

1. **Clone or Download** the project files to your local machine

2. **Install Dependencies**:
   ```bash
   pip install pyftpdlib
   ```

3. **Verify Tkinter** (usually pre-installed with Python):
   ```bash
   python -m tkinter
   ```
   A small window should appear if Tkinter is installed correctly.

## 🚀 Usage

### Step 1: Start the FTP Server

1. Open a terminal/command prompt
2. Navigate to the project directory
3. Run the server:
   ```bash
   python ftp_server.py
   ```
4. You should see:
   ```
   FTP server running at 127.0.0.1:2121
   ```

### Step 2: Launch the FTP Client

1. Open a **new** terminal/command prompt
2. Navigate to the project directory
3. Run the client:
   ```bash
   python ftp_gui_client.py
   ```

### Step 3: Connect and Transfer Files

1. **Default Credentials** (pre-filled):
   - Host: `127.0.0.1`
   - Port: `2121`
   - Username: `user`
   - Password: `12345`

2. Click **Connect** button

3. **To Upload a File**:
   - Select a file from the "Local Files" list (left side)
   - Click **Upload** button
   - Watch the progress bar

4. **To Download a File**:
   - Select a file from the "Remote Files" list (right side)
   - Click **Download** button
   - Watch the progress bar

5. Click **Refresh** to update both file lists

## 🎵 Default Test Files

This project includes several default files for testing file transfer functionality:

### Audio Files
- **voice.wav**: Sample WAV audio file for testing audio file transfers
  - Located in both root directory and `ftp_home` folder

### Video Files
- **vid.mp4**: Sample MP4 video file for testing video file transfers
  - Located in both root directory and `ftp_home` folder

### Text Files
- **test.txt**: Sample text file for testing text file transfers

### Other Files
- **aa.c**: C source code file
- **aa.exe**: Compiled executable file

These files are provided to demonstrate the FTP client's capability to handle various file types including:
- Binary files (audio/video)
- Text files
- Source code files
- Executable files

You can use these files to test upload and download functionality immediately after setting up the server and client.

## 📸 Screenshots

### Application Interface
![FTP Client GUI](../Ref%20Images/Screenshot%202026-01-18%20115122.png)
*Main FTP Client interface showing connection settings and file lists*

### File Transfer in Progress
![File Transfer](../Ref%20Images/Screenshot%202026-01-18%20115149.png)
*File upload/download with progress bar*

### Successful Connection
![Connected View](../Ref%20Images/Screenshot%202026-01-18%20115159.png)
*Connected state showing remote and local files*

## 🔍 Technical Details

### Server Configuration
- **Library**: pyftpdlib
- **Host**: 127.0.0.1 (localhost)
- **Port**: 2121
- **Home Directory**: `./ftp_home`
- **Permissions**: `elradfmwMT` (Full access)
  - e: change directory
  - l: list files
  - r: retrieve files
  - a: append to files
  - d: delete files
  - f: rename files
  - m: create directories
  - w: write files
  - M: file mode
  - T: modify time

### Client Features
- **GUI Framework**: Tkinter
- **FTP Protocol**: ftplib (built-in)
- **Threading**: Prevents UI freezing during transfers
- **Binary Mode**: Ensures integrity of non-text files
- **Progress Tracking**: Real-time file transfer progress
- **Error Handling**: User-friendly error messages

### Transfer Mechanism
- Files are transferred in **binary mode** (TYPE I)
- Chunk size: 1024 bytes
- Progress callback updates GUI in real-time
- Thread-based transfers prevent UI blocking

## 🐛 Troubleshooting

### Server Won't Start
- **Error**: "Address already in use"
  - **Solution**: Another process is using port 2121. Either close it or change the port in both server and client.

### Connection Refused
- **Solution**: Ensure the FTP server is running before starting the client
- Check that firewall isn't blocking port 2121

### Files Not Showing
- Click the **Refresh** button
- Verify you're connected to the server
- Check that `ftp_home` directory exists

### Upload/Download Fails
- Ensure you have selected a file from the list
- Check file permissions
- Verify sufficient disk space

### Progress Bar Not Moving
- This is normal for very small files (transfer happens instantly)
- For larger files, the bar should update smoothly

## 👨‍💻 Development

### Customization Options

1. **Change Server Port**: Modify the `address` tuple in `ftp_server.py`
2. **Change Credentials**: Update username/password in `ftp_server.py`
3. **Change Home Directory**: Modify `home_dir` variable in `ftp_server.py`
4. **Modify GUI**: Edit Tkinter components in `ftp_gui_client.py`

### Future Enhancements
- Multiple user support
- Directory navigation in GUI
- File deletion capability
- Drag-and-drop file upload
- Resume interrupted transfers
- File preview
- Remote directory creation/deletion

## 📝 License

This project is created for educational purposes as part of Computer Networks (CN) coursework.

## 🙏 Acknowledgments

- **pyftpdlib**: Python FTP server library
- **Tkinter**: Python's standard GUI package
- **ftplib**: Python's FTP protocol client library

---

**Course**: Computer Networks (CN) - Semester 4  
**Academic Year**: 2026  
**Project Type**: GUI-based FTP File Transfer Application
