import qrcode

def create_qr_code(data, file_path):
    img = qrcode.make(data)
    img.save(file_path)

if __name__ == "__main__":
    create_qr_code('https://www.example.com', 'qrcode.png')
