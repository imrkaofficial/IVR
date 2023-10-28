# IVR Phone Menu with Tiniyo and Flask

This is a Python Flask application for an IVR (Interactive Voice Response) phone menu system. It uses the Tiniyo API for voice responses and menu navigation.

## Features

- Multilingual support for menu options.
- Call forwarding to Tiniyo executives.
- Specialized options for services like Hello Tunes and Balance Inquiry.
- Easy customization of menu options.

## Prerequisites

Before running this application, ensure you have the following set up:

- Python 3.x
- Flask
- Tiniyo Account with API credentials
- Internet connectivity

## Getting Started

1. Clone this repository to your local machine.
2. Update the `config.py` file with your Tiniyo API credentials.
3. Install the required Python packages using `pip install -r requirements.txt`.
4. Run the application with `python app.py`.

## Usage

- Access the IVR menu by making a GET or POST request to `/ivr/tiniyo`.
- Follow the menu options by pressing digits on your phone.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Author

- Rajat Kumar Goyal

