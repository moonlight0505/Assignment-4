from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
import logging
from datetime import time

# Enable logging for debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)  # Changed to DEBUG to log more details
logger = logging.getLogger(__name__)

# Initialize the Application
application = Application.builder().token("8084937540:AAEVMW_3EJg8sZwmleov6UgxtE0zrArRYEA").build()

# Example user data storage (use a database in production)
user_data = {}

# Track notification settings
user_notifications = {}

# Function to send summary (just a basic example)
async def send_summary(context: CallbackContext):
    user_id = context.job.context
    logger.debug(f"Sending summary to user {user_id}")  # Debugging line
    if user_id in user_data:
        income = user_data[user_id]["income"]
        expenses = user_data[user_id]["expenses"]
        summary_text = f"Summary:\nIncome: {income}\nExpenses: {expenses}"
        await context.bot.send_message(chat_id=user_id, text=summary_text)
    else:
        logger.warning(f"No data found for user {user_id}")  # Debugging line

# Create inline keyboard buttons for notification settings
def notification_buttons():
    keyboard = [
        [InlineKeyboardButton("Enable Daily Summary", callback_data='enable_daily')],
        [InlineKeyboardButton("Enable Weekly Summary", callback_data='enable_weekly')],
        [InlineKeyboardButton("Disable Notifications", callback_data='disable_notifications')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Command to enable notifications
async def notify_on(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    
    # Initialize user notifications if not already set
    if user_id not in user_notifications:
        user_notifications[user_id] = {'daily': False, 'weekly': False}
    
    keyboard = notification_buttons()
    logger.debug(f"Sending inline buttons to user {user_id}")  # Debugging line
    # Send the message with buttons
    await update.message.reply_text("Choose your notification preference:", reply_markup=keyboard)

# Command to handle user clicking on buttons
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user_id = query.message.chat.id

    logger.debug(f"User {user_id} clicked button: {query.data}")  # Debugging line
    
    if query.data == 'enable_daily':
        user_notifications[user_id]['daily'] = True
        await query.edit_message_text("Daily summary notifications are enabled.")
        # Schedule daily summary (every day at 11:59 PM)
        logger.debug(f"Scheduling daily summary for user {user_id} at 11:59 PM.")  # Debugging line
        context.job_queue.run_daily(send_summary, time=time(23, 59), context=user_id)

    elif query.data == 'enable_weekly':
        user_notifications[user_id]['weekly'] = True
        await query.edit_message_text("Weekly summary notifications are enabled.")
        # Schedule weekly summary (every Sunday at 11:59 PM)
        logger.debug(f"Scheduling weekly summary for user {user_id} every Sunday at 11:59 PM.")  # Debugging line
        context.job_queue.run_daily(send_summary, time=time(23, 59), days=(6,), context=user_id)  # 6 = Sunday

    elif query.data == 'disable_notifications':
        user_notifications[user_id] = {'daily': False, 'weekly': False}
        await query.edit_message_text("Notifications are now disabled.")

# Command to start the bot and show a welcome message
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome to your Financial Planner Bot! Use /help to see available commands.")

# Command to show help and usage
async def help_command(update: Update, context: CallbackContext):
    help_text = """
    Available commands:
    /start - Start the bot
    /help - Show this help message
    /config - Configure your income and budgets
    /log - Log income or expense
    /summary - Show your balance and budget summary
    /notifyon - Turn on notifications
    /notifyoff - Turn off notifications
    """
    await update.message.reply_text(help_text)

# Add command handlers for /start, /help, /config, /log, /summary, /notifyon
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("notifyon", notify_on))

# Add handler for button clicks (clicking inline buttons)
application.add_handler(CallbackQueryHandler(button))

# Start the bot polling for messages
application.run_polling()

