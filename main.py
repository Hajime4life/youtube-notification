import requests
import config
from bs4 import BeautifulSoup 

def push_to_telegram(message):
    api_token = config.BOT_TOKEN
    user_ids = config.GROUP_ID
    apiURL = f'https://api.telegram.org/bot{api_token}/sendMessage'
    requests.post(apiURL, json={'chat_id': user_ids,'text': message})
  

def main():
    v_id="e_atyw0IDqg"
    default_video_url = f'https://www.youtube.com/watch?v={v_id}&ab_channel={config.CHANNEL_NAME}' 
    push_to_telegram(default_video_url)

if __name__ == "__main__":
    main()