import os
import socket

def create_file_tree(root_path):
    file_tree = {}
    
    for path, dirs, files in os.walk(root_path):
        for dir in dirs:
            file_tree[dir] = {}
            
        for file in files:
            file_name = os.path.join(path, file)
            file_size = os.path.getsize(file_name)
            file_tree[file] = file_size
    
    return file_tree

# Get the host computer name
hostname = socket.gethostname()

# Get all connected drives
all_drives = [d for d in os.listdir('/') if os.path.isdir(d)]

# Create a file tree for each drive
file_trees = {}
for drive in all_drives:
    file_trees[drive] = create_file_tree(drive)

# Save the file trees to a file
file_name = f'file_trees_{hostname}.txt'
with open(file_name, 'w') as f:
    for drive, tree in file_trees.items():
        f.write(f'File tree for {drive}:\n')
        f.write(str(tree))
        f.write('\n\n')
