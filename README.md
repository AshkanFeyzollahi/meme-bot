# MemeBot

The discord.py bot that uses https://meme-api.com/ to generate
memes and send them to discord servers

## Requirements

* Python >= 3.10 (We Recommend 3.11)
* Pip (Latest)
* git (Latest)

## How to use?

1. Clone this repository by entering this command in terminal/cmd:

    ```bash
    git clone https://github.com/AshkanFeyzollahi/meme-bot.git
    ```

2. Go to that folder which you cloned repository into, and open terminal/cmd
    then run one of these options:

    * Windows

        ```bash
        python -m pip install -r requirements.txt
        ```

    * Linux/MacOS

        ```bash
        python3 -m pip install -r requirements.txt
        ```

    Now you can run bot on your device/host/

3. To run bot, you will need your bot's token, so go to [Discord Developer Portal](https://discord.com/developers/applications)
    and once you create your bot, copy its token and open terminal/cmd in folder
    that you cloned repository to and enter this command:

    ```bash
    echo "BOT_TOKEN={BOT_TOKEN}" > ".env"
    ```

    and also don't forgot to replace `{BOT_TOKEN}` with your bot's token.

4. After doing all task, just open terminal/cmd in same directory and execute
    one of these commands to run bot:

    * Windows

        ```bash
        python main.py
        ```

    * Linux/MacOS

        ```bash
        python3 main.py
        ```

    Once you runned bot, you will receive something like this output:

    ```plain
    Logged in as ...#... (ID: ...)
    ```

    Now go to your discord server and send `?meme` to see that your bot
    sends a meme to your server

## Issues

If you had problem running bot, feel free to open an issue.
