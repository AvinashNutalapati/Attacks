# Password Cracker

A simple Python script to demonstrate a brute force approach to crack a password by interacting with a specific server.

## 🛠️ Dependencies

- Python 3.x
- `requests`: For issuing HTTP requests.

```bash
pip install requests
```

> Note: Although `pandas` and `json` libraries are imported in the script, they are not used and hence, not required.

## 🚀 Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/password-cracker.git
    cd password-cracker
    ```
2. **Run the script**:
    ```bash
    python script.py
    ```

## 🔍 Overview

The script follows these steps:

1. Set up necessary headers and parameters for HTTP requests.
2. Define URLs and payload for the requests.
3. Make an initial POST request to retrieve a token (although the token is hardcoded in this version).
4. In a loop, iterate through a set of characters, appending each character to a string `var` and making a POST request with this new string as the password.
5. Read the `Server-Timing` header from the response to gauge the processing time.
6. Identify the character that results in the longest processing time, append this character to `var`.
7. Repeat steps 4-6 for 20 iterations.
8. Output the cracked password.

## ⚠️ Disclaimer

- The `os` library is imported and there is a provision to exit the script upon an exception, but the corresponding code is commented out.
- The server and endpoints are hardcoded in the script, so you'll need to modify the URLs, parameters, and data to suit your target server.
- Ensure you have necessary permissions to interact with the target server to prevent legal issues. Unauthorized access to computer systems is illegal and punishable by law.

---

Made with ❤️ and Python.
