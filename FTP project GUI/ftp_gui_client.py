import os
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from ftplib import FTP, error_perm
import threading

class FTPClientApp:
    def __init__(self, master):
        self.master = master
        master.title("FTP File Transfer Client")
        master.geometry("700x550")

        self.ftp = None

        # Connection frame
        conn_frame = Frame(master)
        conn_frame.pack(pady=10)

        Label(conn_frame, text="Host:").grid(row=0, column=0)
        self.host_entry = Entry(conn_frame)
        self.host_entry.insert(0, "127.0.0.1")
        self.host_entry.grid(row=0, column=1)

        Label(conn_frame, text="Port:").grid(row=0, column=2)
        self.port_entry = Entry(conn_frame)
        self.port_entry.insert(0, "2121")
        self.port_entry.grid(row=0, column=3)

        Label(conn_frame, text="Username:").grid(row=1, column=0)
        self.user_entry = Entry(conn_frame)
        self.user_entry.insert(0, "user")
        self.user_entry.grid(row=1, column=1)

        Label(conn_frame, text="Password:").grid(row=1, column=2)
        self.pass_entry = Entry(conn_frame, show="*")
        self.pass_entry.insert(0, "12345")
        self.pass_entry.grid(row=1, column=3)

        Button(conn_frame, text="Connect", command=self.connect_ftp).grid(row=2, column=0, columnspan=4, pady=5)

        # Lists frame
        list_frame = Frame(master)
        list_frame.pack(pady=10)

        Label(list_frame, text="Remote Files").grid(row=0, column=0)
        Label(list_frame, text="Local Files").grid(row=0, column=1)

        self.remote_list = Listbox(list_frame, width=40, height=15)
        self.remote_list.grid(row=1, column=0, padx=10)
        self.local_list = Listbox(list_frame, width=40, height=15)
        self.local_list.grid(row=1, column=1, padx=10)

        Button(master, text="Refresh", command=self.load_file_lists).pack(pady=5)

        # Transfer buttons
        transfer_frame = Frame(master)
        transfer_frame.pack()

        Button(transfer_frame, text="Upload", command=self.upload_file).grid(row=0, column=0, padx=10)
        Button(transfer_frame, text="Download", command=self.download_file).grid(row=0, column=1, padx=10)

        # Progress bar
        self.progress = ttk.Progressbar(master, length=600, mode='determinate')
        self.progress.pack(pady=10)

        self.local_dir = os.getcwd()
        self.update_local_files()

    def connect_ftp(self):
        try:
            self.ftp = FTP()
            self.ftp.connect(self.host_entry.get(), int(self.port_entry.get()))
            self.ftp.login(self.user_entry.get(), self.pass_entry.get())
            messagebox.showinfo("Connected", "Connected to FTP server.")
            self.update_remote_files()
        except Exception as e:
            messagebox.showerror("Connection Error", str(e))

    def update_remote_files(self):
        self.remote_list.delete(0, END)
        try:
            files = self.ftp.nlst()
            for file in files:
                self.remote_list.insert(END, file)
        except Exception as e:
            messagebox.showerror("FTP Error", str(e))

    def update_local_files(self):
        self.local_list.delete(0, END)
        files = os.listdir(self.local_dir)
        for file in files:
            self.local_list.insert(END, file)

    def load_file_lists(self):
        self.update_local_files()
        if self.ftp:
            self.update_remote_files()

    def upload_file(self):
        selection = self.local_list.curselection()
        if not selection:
            return
        filename = self.local_list.get(selection[0])
        filepath = os.path.join(self.local_dir, filename)
        threading.Thread(target=self._upload_with_progress, args=(filepath, filename)).start()

    def _upload_with_progress(self, filepath, filename):
        try:
            size = os.path.getsize(filepath)
            self.progress["value"] = 0
            self.progress["maximum"] = size

            self.ftp.voidcmd('TYPE I')  # Binary mode

            with open(filepath, "rb") as f:
                def callback(data):
                    self.progress["value"] += len(data)
                    self.master.update_idletasks()
                self.ftp.storbinary(f"STOR {filename}", f, 1024, callback)

            self.update_remote_files()
            messagebox.showinfo("Upload Complete", f"{filename} uploaded.")
        except Exception as e:
            messagebox.showerror("Upload Error", str(e))

    def download_file(self):
        selection = self.remote_list.curselection()
        if not selection:
            return
        filename = self.remote_list.get(selection[0])
        threading.Thread(target=self._download_with_progress, args=(filename,)).start()

    def _download_with_progress(self, filename):
        try:
            self.ftp.voidcmd('TYPE I')  # Switch to binary mode for size + download
            size = self.ftp.size(filename)
            self.progress["value"] = 0
            self.progress["maximum"] = size

            local_path = os.path.join(self.local_dir, filename)
            with open(local_path, "wb") as f:
                def callback(data):
                    f.write(data)
                    self.progress["value"] += len(data)
                    self.master.update_idletasks()
                self.ftp.retrbinary(f"RETR {filename}", callback)

            self.update_local_files()
            messagebox.showinfo("Download Complete", f"{filename} downloaded.")
        except Exception as e:
            messagebox.showerror("Download Error", str(e))


if __name__ == "__main__":
    root = Tk()
    app = FTPClientApp(root)
    root.mainloop()
