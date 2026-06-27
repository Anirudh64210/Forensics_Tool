import os

def find_exe_files(root_dir):
    exe_files = []
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(".exe"):
                exe_files.append(os.path.join(foldername, filename))
    return exe_files

network_path = r"\\server\share"  # Replace with the network path you want to search
exe_files = find_exe_files(network_path)

for exe_file in exe_files:
    print(exe_file)


"""Replace \\server\share with the actual network path you want to search.
 Keep in mind that this approach will only work if you have proper permissions to access the network folders."""

"""This code assumes that the .exe files are accessible via the network path. If the network requires authentication, you might need to provide credentials using libraries like pywin32.
The code only searches for .exe files in the specified directories and subdirectories. It doesn't perform a deep analysis of the files or their contents.
The os.walk function recursively goes through directories. Depending on the size of the network and the number of files, this process can take a significant amount of time."""