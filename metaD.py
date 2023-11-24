import os
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import subprocess
# filedialog is used to give a browse option in tkinter...
def get_file_metadata(file_path):
    try:
        # Get basic file information
        file_stat = os.stat(file_path)

        # Extract various metadata attributes

        file_size = file_stat.st_size  # File size in bytes
        file_mode = file_stat.st_mode  # File mode (permissions)
        file_owner = file_stat.st_uid  # File owner's user ID
        file_group = file_stat.st_gid  # File owner's group ID
        file_access_time = file_stat.st_atime  # Last access time (timestamp)
        file_modification_time = file_stat.st_mtime  # Last modification time (timestamp)
        file_creation_time = file_stat.st_ctime  # File creation time (timestamp)

        # Convert timestamps to readable format

        access_time_str = time.ctime(file_access_time)
        modification_time_str = time.ctime(file_modification_time)
        creation_time_str = time.ctime(file_creation_time)

        # < decoding owner and group UID >

        if file_owner == 0:
            uid = ">The owner is root(administrator) and has no restrictions\n>Any security checks are bypassed for the owner!"
        else:
            uid = ">Owner has restricted access rights on the system!"

        if file_group == 0:
            gid = ">The group is root(administrator) and has no restrictions\n>any security checks are bypassed for the group!"
        else:
            gid = ">The group has restricted access rights on the system!"

            # < Decoding the mode permissions >

        file_per_oct = oct(file_mode)
        permission = str(file_per_oct)
        if permission[-1] == '7':
            per = ">users have all the permissions(read,write,execute)"
        if permission[-2] == '7':
            per2 = ">group have all the permissions(read,write,execute)"
        if permission[-3] == '7':
            per3 = ">owner have all the permissions(read,write,execute)"
        if permission[-1] == '6':
            per = ">users have the permissions to read and write"
        if permission[-2] == '6':
            per2 = ">group have the permissions to read and write"
        if permission[-3] == '6':
            per3 = ">owner have the permissions to read and write"
        if permission[-1] == '5':
            per = ">users have the permissions to read and execute"
        if permission[-2] == '5':
            per2 = ">group have the permissions to read and execute"
        if permission[-3] == '5':
            per3 = ">owner have the permissions to read and execute"
        if permission[-1] == '4':
            per = ">users have the permissions to read"
        if permission[-2] == '4':
            per2 = ">group have the permissions to read"
        if permission[-3] == '4':
            per3 = ">owner have the permissions to read"
        if permission[-1] == '3':
            per = ">users have the permissions to write and execute"
        if permission[-2] == '3':
            per2 = ">group have the permissions to write and execute"
        if permission[-3] == '3':
            per3 = ">owner have the permissions to write and execute"
        if permission[-1] == '2':
            per = ">users have the permissions to write"
        if permission[-2] == '2':
            per2 = ">group have the permissions to write"
        if permission[-3] == '2':
            per3 = ">owner have the permissions to write"
        if permission[-1] == '1':
            per = ">users have the permissions to execute"
        if permission[-2] == '1':
            per2 = ">group have the permissions to execute"
        if permission[-3] == '1':
            per3 = ">owner have the permissions to execute"

        # Encryption status:
        file_path_enc = file_path
        try:
            result = subprocess.run(['manage-bde', '-status', file_path_enc], capture_output=True, text=True)
            output = result.stdout
            if "Protection Status: On" in output:
                enc1 = f'{file_path},\nThis file is encrypted!'
            else:
                enc1 = f'{file_path} ,\nThis file is not encrypted! '
        except:
            enc1 = "No Encrypting softwares found! Or there are no encryptions!"

        # INSERTING INTO THE TKINTER WINDOW

        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f'File: {file_path}\n')
        result_text.insert(tk.END, f"Size: {file_size} bytes\n")
        result_text.insert(tk.END, f"Mode (Permissions): {oct(file_mode)}\n")
        result_text.insert(tk.END, f"Owner UID: {file_owner}\n")
        result_text.insert(tk.END, f"Group GID: {file_group}\n")
        result_text.insert(tk.END, f"Last Access Time: {access_time_str}\n")
        result_text.insert(tk.END, f"Last Modification Time: {modification_time_str}\n")
        result_text.insert(tk.END, f"File Creation Time: {creation_time_str}\n")
        result_text.insert(tk.END, f"----------------------------------------\n")
        result_text.insert(tk.END, f"Mode (Permissions): {oct(file_mode)}\n")
        result_text.insert(tk.END, f"The permission mode given above is in octal format:\n")
        result_text.insert(tk.END, f"{per}\n")
        result_text.insert(tk.END, f"{per2}\n")
        result_text.insert(tk.END, f"{per3}\n")
        result_text.insert(tk.END, f"----------------------------------------\n")
        result_text.insert(tk.END, f"More details about the file owner and group:\n")
        result_text.insert(tk.END, f"Owner UID: {file_owner}\n")
        result_text.insert(tk.END, f"Group GID: {file_group}\n")
        result_text.insert(tk.END, f"{uid}\n")
        result_text.insert(tk.END, f"{gid}\n")
        result_text.insert(tk.END, f"----------------------------------------\n")
        result_text.insert(tk.END, f"Encryption status of the file:\n")
        result_text.insert(tk.END, f"{enc1}\n")
        result_text.config(state=tk.DISABLED)


    except FileNotFoundError:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: File '{file_path}' not found.\n")
        result_text.config(state=tk.DISABLED)
    except Exception as e:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"An error occurred: {e}\n")
        result_text.config(state=tk.DISABLED)


def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)
        get_file_metadata(file_path)


# Create the main window
window = tk.Tk()
window.title("File Metadata Viewer")
#Disable the resizable Property
window.resizable(False, False)
window.config(bg="#F0F8FF")
# adding icon to the windowbar
photo = PhotoImage(file="logoimg.png")
window.iconphoto(False, photo)

# Create widgets
# main_frame
file_label = tk.Label(window, text="Enter the path to the file:", font="Times 12 bold", bg='#F0F8FF')
file_entry = tk.Entry(window, width=50)
browse_button = tk.Button(window, text="Browse", command=browse_file,
                          activebackground='black', font="Times 10 bold", activeforeground='#F0F8FF',
                          background='#F0F8FF', height=1, width=13, borderwidth=1, relief='ridge', cursor='hand2')
result_text = tk.Text(window, height=26, width=61, state=tk.DISABLED)

# Place widgets on the window
file_label.pack(pady=10)
file_entry.pack(pady=8)
browse_button.pack(pady=8)
result_text.pack(pady=10)

# Run the GUI main loop
window.mainloop()

# --------------------

# The constant tk. END refers to the position after the existing text.
# The constant tk. INSERT refers to the current position of the insertion cursor.

# What does root user mean?
#
# Root is the superuser account in Unix and Linux.
# It is a user account for administrative purposes, and typically has the highest access rights on the system.
# Usually, the root user account is called root .
# However, in Unix and Linux, any account with user id 0 is a root account, regardless of the name.