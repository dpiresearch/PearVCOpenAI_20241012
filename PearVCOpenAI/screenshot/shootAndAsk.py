import base64
import requests
import os
import time

from PIL import ImageGrab
import time

# OpenAI API Key
api_key = os.getenv("OPENAI_API_KEY")
# Step 1: Take a screenshot and save it locally
def take_screenshot():
    screenshot = ImageGrab.grab()
    # filename = f"screenshot_{int(time.time())}.png"
    filename = f"screenshot_.png"
    screenshot.save(filename)
    return filename


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def take_ss():

  # Path to your image
  # image_path = "screenshot.png"
  image_path = take_screenshot()

  # Getting the base64 string
  base64_image = encode_image(image_path)

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What’s in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

  response_json = response.json()
  print(response_json)

  content = response_json['choices'][0]['message']['content']

  current_timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

  # Combine timestamp with content
  combined_string = f"Timestamp: {current_timestamp}\n\n{content}\n\n"

  with open('output.txt', 'a') as file:  # 'a' mode for appending
    file.write(combined_string)

import schedule
import time

# Schedule the function to run every 10 seconds
schedule.every(10).seconds.do(take_ss)

# Infinite loop to keep the schedule running
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for a short interval to avoid high CPU usage


take_ss()
