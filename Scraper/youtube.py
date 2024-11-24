import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

data = []
youtube_video_url = "https://www.youtube.com/watch?v=0LYmM9TgR8I"

service = Service(r'C:\webdrivers\chromedriver.exe')

with Chrome(service=service) as driver:
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get(youtube_video_url)

    for item in range(10):
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(5)  
    comment_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text")))

    for comment in comment_elements:
        data.append(comment.text)

df = pd.DataFrame(data, columns=['comment'])
df.to_csv('scraper/dataset/yt_comment.csv', index=False, encoding='utf-8')
print(df.head())
