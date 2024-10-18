import os
print("Current working directory:", os.getcwd())
print("Files in the app directory:", os.listdir('app'))

from app import App  # Adjust this line if needed

if __name__ == "__main__":
    app = App()  # Instantiate an instance of App
    app.start()  # Start the application
