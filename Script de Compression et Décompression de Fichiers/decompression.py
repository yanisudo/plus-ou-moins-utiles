import zipfile

def decompress_files(zip_name, extract_to):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_to)

if __name__ == "__main__":
    decompress_files('compressed_files.zip', 'path/to/extract/directory')
