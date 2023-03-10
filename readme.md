# Telegramshot

Telegramshot uses PIL and telegram bot API to share screenshots at set intervals.
Information on how to set up Telegram bots is found here:

´´´
https://core.telegram.org/bots#how-do-i-create-a-bot
´´´

Further information on how to get the chatID (place where the screenshots are sent)
is found here: 

´´´
https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
´´´

The default screenshot interval has been set to 15 minutes.

## Compilation and how to run

Compile Telegramshot.exe by running pyinstaller --onefile telegramshot.py within the
same directory.
The resulting telegramshot.exe requires two arguments and has one optional one:

--apiToken <string> [required]

--chatID <string> [required]

--timeDelta <int> [optional]

## Environment

An environment file has been provided.
The current environment uses Python 3.7 for backwards compatibility with older
Windows machines.
Newer versions can be used without any issue.