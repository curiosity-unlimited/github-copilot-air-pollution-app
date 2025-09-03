# Air Pollution App
- This application allows users to retrieve and display air pollution data for locations around the world using OpenWeather's APIs.
- This is a demo app from the course - GitHub Copilot

## Features
- `edit-mode` and `agent-mode` branches can be found.
    - If you're working on Edit mode from the course, please checkout to the `edit-mode`.
    - If you're working on Agent mode from the course, please checkout to the `agent-mode`.
- From there, you can compare your progress with this project, commit-by-commit, step-by-step. Just checkout to specific commit as the Setup section described below.
- There's also a file named `PROMPTS.md` where you can find all the prompts that are used in this course.
- Secure API key handling using environment variables (.env file)
- Air quality data retrieval and display for any location worldwide

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/curiosity-unlimited/github-copilot-air-pollution-app.git
   cd github-copilot-air-pollution-app
   ```

2. Fetch all the branches:
    ```
    git fetch --all
    ```

3. Check all the branches and make sure `edit-mode` and `agent-mode` are in the list:
    ```
    git branch -a
    ```

4. Checkout to `edit-mode` if you're working on Edit mode from the course:
    ```
    git checkout edit-mode
    ```

5. Checkout to `agent-mode` if you're working on Agent mode from the course:
    ```
    git checkout agent-mode
    ```

6. Checkout to specific commit or step if necessary:
    ```
    git checkout <commit-hash>
    ```

7. Install dependencies using uv:
    
    This project uses [uv](https://docs.astral.sh/uv/) for dependency management. If you don't have uv installed, you can install it following the instructions on their [website](https://docs.astral.sh/uv/installation/).
    
    ```
    # Create a virtual environment and install dependencies
    uv venv
    source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
    uv sync
    
    # To add new dependencies
    uv add <python-package>
    ```

8. Set up your API key:

    This application requires an API key from [OpenWeatherMap](https://openweathermap.org/). 
    
    ```
    # Create a .env file in the root directory based on the example
    cp .env.example .env
    # Then edit the .env file to add your actual API key
    ```
    
    **IMPORTANT**: The `.env` file contains sensitive information and is included in `.gitignore` to prevent it from being committed to version control. Never share your API key or commit it to the repository.

## License

[MIT](LICENSE)
