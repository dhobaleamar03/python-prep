import os

#read settings from the environment, using defaults when missing.
config = {
    "app_name": os.getenv("APP_NAME", "My Python API"),
    "debug": os.getenv("DEBUG", "False").lower() == "true",
    "port": int(os.getenv("PORT", "5000"))
}

#display the current application settings.
print("Application:", config["app_name"])
print("Debug mode:", config["debug"])
print("Port:", config["port"])
