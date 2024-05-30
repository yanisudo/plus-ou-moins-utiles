from PIL import ImageGrab

def capture_screen(file_path):
    screen = ImageGrab.grab()
    screen.save(file_path)

if __name__ == "__main__":
    capture_screen('screenshot.png')
