# Owncast_chat_webhook
Quick Webhook for using Owncast chat with OBS

# Installing deps

``` bash
poetry install
```

# Configuration

Edit `server.py`, and choose a file that you want to write the chatlog to.

Change the line with `FILE_TO_WRITE_TO` to point to a file read from OBS.

# Run

``` bash
poetry run python server.python
```

Now you will need to create and point a chat webhook in Owncast to point to your running webhook listener.

Note that it will tell you the host/port combination that you will need to put in the Owncast webhook. Make sure to remember to add `/webhook` to the end of the URI.
Profit.
