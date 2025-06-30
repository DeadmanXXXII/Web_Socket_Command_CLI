
# Web-Socked: WebSocket Command Injection Tester

## Table of Contents
- [About](#about)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Graphical User Interface (GUI) Mode](#graphical-user-interface-gui-mode)
  - [Command-Line Interface (CLI) Mode](#command-line-interface-cli-mode)
- [How It Works](#how-it-works)
- [Disclaimer & Ethical Use](#disclaimer--ethical-use)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## About

`Web-Socked` is a versatile Python tool designed to assist cybersecurity professionals in identifying and verifying WebSocket-based command injection vulnerabilities in web applications. It allows you to inject arbitrary commands into WebSocket messages and then check an external HTTP endpoint to confirm the command's execution and its impact.

Developed as part of the [Cyfrin Updraft Smart Contract Security Auditor Course](https://updraft.cyfrin.io/), this tool showcases the principles of identifying and exploiting vulnerabilities across different communication protocols, aligning with a proactive stance on AI integration in cybersecurity – enabling people and machines to achieve a higher standard of security testing together.

## Features

-   **Dual Operation Modes:**
    -   **GUI Mode:** User-friendly Tkinter-based interface for interactive testing.
    -   **CLI Mode:** Command-line arguments for automation and scripting integration.
-   **WebSocket Command Injection:** Crafts and sends specially formatted messages over WebSocket connections to attempt command execution.
-   **Response Monitoring:** Waits for a specified keyword in the WebSocket response to confirm message delivery/processing.
-   **External Verification:** Checks a separate HTTP/S URL for a success keyword to confirm the arbitrary command's execution and its visible effects.
-   **Clear Feedback:** Provides immediate success or failure notifications.

## Prerequisites

Before using `Web-Socked`, ensure you have Python 3.x installed on your system. You will also need the following Python libraries:

-   `requests`
-   `websocket-client`
-   `tkinter` (usually comes pre-installed with Python, but confirm if you encounter GUI issues)

#  Installation

1.  **Clone the repository (or copy the code):**

    ```bash
    git clone [https://github.com/YourUsername/web-socked.git](https://github.com/YourUsername/web-socked.git)
    cd web-socked
    ```
    *(Note: Replace `YourUsername` with your actual GitHub username if you create a repository for this.)*

2.  **Install the required Python packages:**

    ```bash
    pip install requests websocket-client
    ```
    *(`tkinter` is typically part of standard Python installations.)*

## Usage

You can use `Web-Socked` in two distinct ways: via its interactive GUI or through command-line arguments.

### Graphical User Interface (GUI) Mode

To run the tool with its graphical interface, execute the script directly:

```bash
python your_script_name_gui.py
```

*(Assuming you've saved the first script as `your_script_name_gui.py`)*

The GUI will prompt you for the following inputs:

  - **WebSocket URL:** The full URL of the target WebSocket endpoint (e.g., `ws://example.com/ws` or `wss://example.com/socket`).
  - **Command to Inject:** The malicious command you wish to execute on the target server (e.g., `id`, `ls -la /tmp`, `cat /etc/passwd`).
  - **Response Keyword:** A string expected in the WebSocket's immediate response to indicate the message was received/processed.
  - **URL to Check for Success:** An HTTP/S URL where the results of your command injection might be visible (e.g., a log file, a directory listing, or an API endpoint that reflects system information).
  - **Success Keyword:** A string expected within the content of the `URL to Check for Success` that confirms your command was successfully executed.

### Command-Line Interface (CLI) Mode

For automated testing or scripting, use the CLI mode. Execute the script with the required arguments:

```bash
python your_script_name_cli.py \
    --websocket-url "ws://[example.com/socket](https://example.com/socket)" \
    --command "whoami" \
    --response-keyword "subscribed" \
    --check-url "[http://example.com/logs/activity](http://example.com/logs/activity)" \
    --success-keyword "root"
```

*(Assuming you've saved the second script as `your_script_name_cli.py`)*

**Arguments:**

  - `--websocket-url` (required): The WebSocket URL.
  - `--command` (required): The command to inject.
  - `--response-keyword` (required): Keyword expected in WebSocket response.
  - `--check-url` (required): HTTP/S URL to verify command success.
  - `--success-keyword` (required): Keyword expected in the check URL's response.

## How It Works

The core of `Web-Socked` lies in its `GenericSolver` (GUI) or `WebSocketCommandInjection` (CLI) class. The process involves two main steps:

1.  **WebSocket Command Injection (`send_command_via_websocket`):**

      - Establishes a connection to the specified WebSocket URL.
      - Constructs a special message format: `Hello, I would like to subscribe to the newsletter. This is my email address: attacker@example.com | {YOUR_COMMAND}.`
      - This format is crafted to exploit common scenarios where applications might take user-supplied input (like an email address) and directly pass it to a shell command or system function without proper sanitization. The `|` (pipe) character is often used in shell environments to chain commands.
      - Sends this message as a JSON object over the WebSocket.
      - Listens for a response from the WebSocket and continues to receive messages until the `response_keyword` is found, indicating a successful initial interaction.

2.  **Success Verification (`check_success`):**

      - After the WebSocket interaction, the tool makes a standard HTTP GET request to the `check_url`.
      - This `check_url` is assumed to be an endpoint where the side effects of a successful command injection would be visible (e.g., server logs, files created by the command, specific system information reflecting the command's output).
      - It then parses the response content of this HTTP request, looking for the `success_keyword`.
      - If the `success_keyword` is present, it signifies that the injected command was likely executed successfully on the server, and its output or effect was reflected at the `check_url`.

## Disclaimer & Ethical Use

This tool is intended **solely for educational purposes, security research, and authorized penetration testing.** Do not use `Web-Socked` against any system or network for which you do not have explicit permission. Unauthorized access to computer systems is illegal and unethical. The author is not responsible for any misuse or damage caused by this software. **Always obtain proper authorization before testing.**

## Contributing

Feel free to fork this repository, open issues, or submit pull requests. Contributions are welcome to enhance functionality, improve reliability, or expand testing capabilities.

## License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
*(You'll need to create a `LICENSE` file in your repository if you choose the MIT license.)*

## Acknowledgements

  - Built by DeadmanXXXII

<!-- end list -->
```
