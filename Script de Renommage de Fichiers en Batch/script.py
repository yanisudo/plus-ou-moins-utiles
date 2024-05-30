import os

def rename_files(directory, prefix):
    for count, filename in enumerate(os.listdir(directory)):
        dst = f"{prefix}_{str(count)}{os.path.splitext(filename)[1]}"
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, dst)
        os.rename(src, dst)

if __name__ == "__main__":
    rename_files('path/to/your/directory', 'new_prefix')
