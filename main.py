import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
EMAIL = '#'
PWD = '#'
driver = webdriver.Chrome()
driver.get("https://tinder.com/app/profile")

login_button = driver.find_element(By.LINK_TEXT, "Log in")
login_button.click()
time.sleep(20)
facebook_login = driver.find_element(By.XPATH, '#')
facebook_login.click()
time.sleep(10)

# In Selenium, each window has a identification handle, we can get all the window handles with:
windows = driver.window_handles
# The above line of code returns a list of all the window handles. The first window is at position 0 e.g.
base_window = windows[0]
# New windows that have popped out from the base_window are further down in the sequence e.g.
fb_login_window = windows[1]
# We can switch our Selenium to target the new facebook login window by:
driver.switch_to.window(fb_login_window)
# You can print the driver.title to verify that it's the facebook login window that is currently target:
print(driver.title)
# If successful the printed title should be "Facebook" and not "Tinder | Match. Chat. Date."

email_entry = driver.find_element(By.ID, "email")
email_entry.send_keys(EMAIL)
pwd_entry = driver.find_element(By.ID, 'pass')
pwd_entry.send_keys(PWD)
pwd_entry.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
print(driver.title)
# Tinder | Dating, Make Friends & Meet New People means successful action
time.sleep(10)
# Allowing Location
location = driver.find_element(By.XPATH, '#')
location.click()
time.sleep(10)
# Disable notifications
notifications = driver.find_element(By.XPATH, '#')
notifications.click()
time.sleep(10)
#Allow cookies
cookies = driver.find_element(By.XPATH, '#')
cookies.click()
time.sleep(5)
# Likes
like = driver.find_element(By.XPATH, '#')
for n in range(100):
    time.sleep(5)
    like.click()
    time.sleep(5)
try:
    print("called")
    like = driver.find_element(By.XPATH, '#')
    like.click()

# Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
except ElementClickInterceptedException:
    try:
        match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
        match_popup.click()

    # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
    except NoSuchElementException:
        time.sleep(2)
