# Python Flask sample for Azure App Service (Linux)

This is a sample Flask app that demonstrates a few features of the framework.

## Running the app

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   flask run
   ```

## Endpoints

* `/`: Returns a simple HTML page.
* `/<name>`: Returns a personalized greeting. For example, `/world` will return "Hello, world!".
* `/json`: Returns a JSON response.
