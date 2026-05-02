import time
import csv
import pandas as pd
import pyautogui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# -------------------------
# Configuration
# -------------------------

USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"
LOGIN_URL = "https://your-ciw-portal-url"

INPUT_FILE = "claims_input.csv"
OUTPUT_FILE = "claims_output.csv"

# -------------------------
# Start Browser
# -------------------------

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get(LOGIN_URL)

time.sleep(3)

# -------------------------
# Login
# -------------------------

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)

login_button = driver.find_element(By.ID, "loginButton")
login_button.click()

time.sleep(5)

actions = ActionChains(driver)

# -------------------------
# Hover Search Menu
# -------------------------

search_menu = driver.find_element(By.ID, "searchMenu")

actions.move_to_element(search_menu).perform()

time.sleep(2)

claims_button = driver.find_element(By.ID, "claimsButton")
claims_button.click()

time.sleep(3)

# -------------------------
# Read Input Claims
# -------------------------

claims = pd.read_csv(INPUT_FILE)

results = []

# -------------------------
# Loop Claims
# -------------------------

for index, row in claims.iterrows():

    claim_id = row["claim_id"]

    # Hover right side panel
    right_panel = driver.find_element(By.ID, "rightPanel")

    actions.move_to_element(right_panel).perform()

    time.sleep(2)

    # Focus ClaimID field using PyAutoGUI
    pyautogui.click(500, 400)

    claim_field = driver.find_element(By.ID, "claimIdField")
    claim_field.clear()
    claim_field.send_keys(claim_id)

    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()

    time.sleep(4)

    # Extract details
    name = driver.find_element(By.ID, "memberName").text
    date = driver.find_element(By.ID, "serviceDate").text
    provider = driver.find_element(By.ID, "providerName").text

    results.append({
        "ClaimID": claim_id,
        "MemberName": name,
        "ServiceDate": date,
        "Provider": provider
    })

# -------------------------
# Save CSV
# -------------------------

df = pd.DataFrame(results)
df.to_csv(OUTPUT_FILE, index=False)

print("Report generated:", OUTPUT_FILE)

driver.quit()