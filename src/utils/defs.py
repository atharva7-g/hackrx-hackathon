import os
import sys
import getpass


# Automatically resolve and inject the project root into sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


CHUNK_SIZE = 800
CHUNK_OVERLAP = 100

def config_init():
    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")