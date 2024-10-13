from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from PIL import ImageGrab
import time

# Step 1: Take a screenshot and save it locally
def take_screenshot():
    screenshot = ImageGrab.grab()
    # filename = f"screenshot_{int(time.time())}.png"
    filename = f"screenshot_.png"
    screenshot.save(filename)
    return filename

# Step 2: Authenticate and create a Google Drive instance
def authenticate_google_drive():
    gauth = GoogleAuth()
    # This will prompt you to log in via the browser and authorize the app
    gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication
    drive = GoogleDrive(gauth)
    return drive

# Step 3: Upload the file to Google Drive
def upload_to_google_drive(drive, file_path):
    file = drive.CreateFile({'title': file_path})
    file.SetContentFile(file_path)
    file.Upload()
    print(f"File '{file_path}' uploaded successfully to Google Drive.")

if __name__ == "__main__":
    # Step 1: Take the screenshot
    screenshot_file = take_screenshot()

    # Step 2: Authenticate Google Drive
    #drive = authenticate_google_drive()

    # Step 3: Upload the screenshot to Google Drive
    #upload_to_google_drive(drive, screenshot_file)

