# Financial Planner Bot
A simple Telegram bot to help users manage their finances by logging income, setting budgets, viewing financial summaries, and receiving daily/weekly notifications. The link to the bot: http://t.me/myfinaceplan_bot (you can create yours)

## Features:

Configure Income & Budgets: Set income and budgets for different categories.

Log Income & Expenses: Log income and expenses under specific categories.

View Balance & Budget Summaries: View your financial balance and budget status.

Push Notifications: Receive daily or weekly summaries and budget alerts.

Commands:

/start: Start the bot and display available commands.

/help: Get a list of commands and instructions.

/config: Configure income and budget settings.

/log: Log income or expenses.

/summary: View a summary of income, expenses, and budgets.

/notifyon: Enable daily or weekly summaries.

/notifyoff: Disable notifications.

Setup Instructions:
1. Install the required libraries with the following command:
pip install python-telegram-bot

3. Set Up Your Telegram Bot
Open BotFather in Telegram.
Create a new bot and get the API token.
Replace the YOUR_API_KEY placeholder in the code with your actual bot token.

3. Run the Bot
Once everything is set up, you can run the bot using the following command:
python financial_planner_bot.py
The bot will start and be available for interaction on Telegram.

4. Interacting with the Bot
Once the bot is running, here are the key commands you can use:

/start: Start interacting with the bot.

/help: Get a list of all available commands.

/config: Configure your income and budgets.

/log: Log income or expenses under a category.

/summary: View your balance and budget summary.

/notifyon: Enable daily or weekly notifications.

/notifyoff: Disable notifications.

Example Usage
Configure Income:
/config
Set Budget:
/set_budget 500 rent
Log Income:
/log income 1000 salary
Log Expense:
/log expense 200 rent
View Summary:
/summary
Enable Notifications:
/notifyon
Disable Notifications:
/notifyoff

The bot stores user data (income, expenses, budgets, notifications) in a JSON file (user_data.json).
