import requests
import time

# Apna bot token yahan paste karo (baad mein change karna)
BOT_TOKEN = "8668883924:AAGQgk2dq3tRoeRmOiWbP4NH6QDAAmq2gBU"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_updates(offset=None):
    url = TELEGRAM_URL + "/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()["result"]

def send_message(chat_id, text):
    url = TELEGRAM_URL + "/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

def handle_message(message):
    text = message.get("text")
    chat_id = message["chat"]["id"]
    
    if text == "/start":
        send_message(chat_id, "👋 Salam! Main student help bot hoon.\n\nCommands:\n/help - Madad\n/about - Bot ke baare mein")
    
    elif text == "/help":
        send_message(chat_id, "Available commands:\n/start - Start bot\n/help - Show help\n/about - About bot")
    
    elif text == "/about":
        send_message(chat_id, "🤖 Student Help Bot\nVersion 1.0\nMade with ❤️ for students")
    
    else:
        send_message(chat_id, f"Aapne likha: {text}\n\n/help dekh kar commands use karein.")

def main():
    print("Bot start ho raha hai...")
    last_update_id = 0
    
    while True:
        try:
            updates = get_updates(last_update_id + 1)
            for update in updates:
                if "message" in update:
                    handle_message(update["message"])
                    last_update_id = update["update_id"]
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(3)

if __name__ == "__main__":
    main()
