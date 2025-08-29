from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")

def main():
    print("Hello from github-copilot-air-pollution-app!")


if __name__ == "__main__":
    main()
