import os

#use the configured app name, or a default if it isn't set.
app_name = os.getenv("APP_NAME", "My Python API")

print("Application:", app_name)
