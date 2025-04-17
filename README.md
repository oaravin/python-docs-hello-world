---
page_type: sample
description: "A minimal sample app that can be used to demonstrate deploying Flask apps to Azure App Service on Linux."
languages:
- python
products:
- azure
- azure-app-service
---

# Python Flask sample for Azure App Service (Linux)

This is a minimal Flask app that can be deployed to Azure App Service on Linux.

For instructions on running and deploying the code, see [Quickstart: Create a Python app in Azure App Service on Linux](https://docs.microsoft.com/azure/app-service/quickstart-python).

## Running Locally

1.  **Prerequisites:** Ensure you have Python 3 installed (Python 3.7+ recommended).
2.  **Clone the repository:**
    ```bash
    git clone https://github.com/Azure-Samples/python-docs-hello-world
    ```
3.  **Navigate to the project directory:**
    ```bash
    cd python-docs-hello-world
    ```
4.  **Create and activate a virtual environment (recommended):**
    *   On Linux/macOS:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
5.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
6.  **Run the application:**
    ```bash
    flask run
    ```
    You should see output indicating the server is running, typically on `http://127.0.0.1:5000/`.

## Usage

Once the application is running, open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

You should see the message "Hello, World!".

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
