import zipfile
import os

def compress_files(directory, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, os.path.relpath(file_path, directory))

if __name__ == "__main__":
    compress_files('path/to/your/directory', 'compressed_files.zip')
