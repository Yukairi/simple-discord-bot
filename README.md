# simple-discord-bot
REMEMBER THAT DISCORD BOT TOKEN IS DIFFERENT FROM EVERYONE, IT IS A UNIQUE TOKEN THAT SHOULDNT BE ALLOWED TO BE SHARED PUBLICLY


This Python code provides a simple chatbot functionality with specific commands. The chatbot responds to various messages, including greetings, dice rolling, help requests, and mathematical expressions. Additionally, it supports vector operations like addition, subtraction, and scaling.

Install proper libraries such as
pip install discord.py

Features

Message Handling
The bot listens for messages in the Discord server and processes them.


Command Prefix
Commands are initiated with a question mark ('?') as a prefix. For example, ?hello.

Responses
The bot uses the responses module to generate responses based on user messages.

Responses are sent to the same channel where the command was received.

Private Responses
If a message starts with a question mark ('?'), the bot sends a private response.

1 Copy and paste the provided code into a Python file (e.g., discord_bot.py).

2 Replace the placeholder token in the TOKEN variable with your Discord bot token.

3 Run the Python script to start the bot.

Dependencies:
discord.py

Configuration
Replace the placeholder in the TOKEN variable with your Discord bot token.
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'


Running the Bot  
Execute the script to run the Discord bot.
python discord_bot.py


Notes
Ensure that the bot has the necessary permissions in the Discord server.
Customize the code and responses in the responses.py module to suit your needs.
Feel free to modify the code and experiment with different responses and commands!

How to Use:

1 Ensure you have Python installed on your system.

2 Copy and paste the code into a Python file (e.g., chatbot.py).

3 Run the Python script.

4 Send messages to the chatbot and receive responses.


Features

1 Greetings

2 Send a message containing 'hello' to receive a special greeting from the hydro archon.

3 Dice Rolling

4 Send the command '!dice' to roll a six-sided die and receive the result.

Help

1 Send the command '!help' to receive a help message (modifiable).



Mathematical Expressions

Send mathematical expressions with the commands '!add', '!sub', '!mul', '!div'.

Example: !add 2 + 3

Vector Operations

Send vector operations using commands like 'vector add', 'vector subtract', 'vector scale'.

Example: vector add 1,2,3 4,5,6

EXAMPLE FUNCTIONS
message = "hello"
response = get_response(message)
print(response)

message = "!dice"
response = get_response(message)
print(response)

message = "!help"
response = get_response(message)
print(response)

message = "!add 2 + 3"
response = get_response(message)
print(response)

message = "vector add 1,2,3 4,5,6"
response = get_response(message)
print(response)


Notes

Modify the help message in the !help command according to your needs.

Ensure proper syntax for mathematical and vector commands.

Feel free to customize the code and experiment with different messages and commands!
