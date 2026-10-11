Telegram Country Info Bot

A Telegram bot built with Python that retrieves country information using the `CountryInfo` library and returns the results to users through Telegram.

Features

- Retrieve country information based on user input
- Use the CountryInfo Python library
- Deliver results directly through Telegram
- Secure bot token management using `python-dotenv`

Technologies Used

- Python
- pyTelegramBotAPI
- CountryInfo
- python-dotenv

Configuration

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:

   ```env
   TOKEN=your_telegram_bot_token_here
   ```

5. Load the token using `python-dotenv` and access it through `os.getenv()`.
6. Run the bot and interact with it in Telegram.

Environment Variables

The Telegram bot token is stored in the `.env` file to keep it separate from the source code. Never upload the actual token to a public repository.
