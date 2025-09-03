# Prompts
These are the prompts that we use for our demo project, Air Pollution App, from course - GitHub Copilot

## Usage
- You can copy and paste these prompts directly from this file so that you don't have to stop the course video then type them manually.
- However, when you see symbols like context (#), extensions (@) or commands (/) in the prompt, you'll need to remove that specific part from the prompt and type again so that proper content can be brought out in the Chat window.
- For example, when you see #file:main.py in a prompt, you should remove #file:main.py and type "#mai".. so that GitHub Copilot can search that file for you. And then you should select that file from suggestions that GitHub Copilot provides and then the #file:main.py should be covered with blue color.

## Content
### 使用 Ask 模式
- "What is uv and what does it do?"
- "What is uv, https://docs.astral.sh/uv/, and what does it do?"
- "What is virtual environment in Python, and what advantages does it have?"
- "Are there any other Python tools similar to uv?"
- "How can I install uv on my macOS?"
- "How can I initialize a Python project with uv, install a specific Python version, and create a virtual environment for my project?"

### 使用 Edit 模式
- "What's the problem of putting API Key here directly?"
- "I'd like to install python-dotenv and use .env file to store this API Key"
- "I'd like to install python-dotenv and use .env file to store this API Key, please remember to exclude the .env file from version control"
- "This python project is managed by uv, https://docs.astral.sh/uv/, what's the best practice to install new python packages?"
- "What's the purpose of this file?"
- "Let user provide location as input, and create a function to use the API key and Geocoding API from Open Weather, https://openweathermap.org/, to get longitude and latitude as output"
- "How to fix this error?"
- "How to fix #terminalSelection?"
- "How to fix the #problems?"
- "Please separate API request logic from #file:main.py"
- "Please add a function in a new file named utils.py that verifies both longitude and latitude fall within a reasonable range, and make sure it applies to #file:api_requests.py or #file:main.py if necessary."
- "Create a function that takes longitude and latitude from #file:api_requests.py's output as input, and use the API key and Air Pollution API from Open Weather, to get air pollution as output. Please also use this function in #file:main.py to print output data."
- "What is PEP 484?"
- "Please modify functions in #file:api_requests.py so that it complies with PEP 484 (type hints)"
- "Please also modify functions in #selection so that it complies with PEP 484 (type hints)"

### 使用 Agent 模式
- "I need to use Open Weather's Geocoding API and Air Pollution API, https://openweathermap.org/, to let user input location and get air pollution data while handling API Key in #file:.env securely."
- "We use uv, https://docs.astral.sh/uv/, to manage this project, please remember to add `uv.lock` file, and reflect current changes in #file:README.md. We prefer to use `uv add <python-package>` or `uv sync`."
- "For security reasons, please remember to include #file:.env in #file:.gitignore and also address this matter in #file:README.md"
- "Please add a function in #file:utils.py that verifies both longitude and latitude fall within a reasonable range, and make sure it applies to #file:api_requests.py or #file:main.py if necessary."