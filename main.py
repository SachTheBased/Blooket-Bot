import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

print("Starting up...")

info = {
    "email": "",
    "password": ""
}

tokens = 500
#
driver = webdriver.Chrome('./chromedriver')
wait = WebDriverWait(driver, timeout=10)
driver.get("https://id.blooket.com/login")


def smart_wait(by, value):
    return wait.until(EC.presence_of_element_located((by, value)))


def login():
    time.sleep(0.5)

    email = smart_wait(By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[4]/input')
    password = smart_wait(By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[5]/input')
    submit = smart_wait(By.XPATH, '//*[@id="app"]/div/div/div[2]/form/input')

    email.send_keys(info["email"])
    password.send_keys(info["password"])

    submit.click()

def start():
    driver.get("https://play.blooket.com/solo?id=6325daba3a2814f9d65eb511")

    time.sleep(0.5)

    gamemode = smart_wait(By.CSS_SELECTOR, '[alt="Café"]')
    gamemode.click()

    time.sleep(0.5)
    # //*[@id="app"]/div/div/div[2]/div[3]/div[2]/div[2]
    if smart_wait(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div[1]').text == "Load Game":
        newgame = smart_wait(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div[2]')
        newgame.click()
    else:
        newgame = smart_wait(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div[1]')
        newgame.click()

    try: slot = smart_wait(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[3]/div[2]/div[6]')
    except: slot = smart_wait(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[3]/div[2]/div[2]')

    if slot.text == "Replace Game":
        slot.click()

        time.sleep(0.5)

        con = smart_wait(By.XPATH, '//*[@id="app"]/div/div/div[3]/form/div[2]/div/div[1]/div[3]')
        con.click()

        time.sleep(0.5)

        mult = smart_wait(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/div/div[2]/div[2]/div[1]')
        mult.click()

        time.sleep(10)

        thanks = smart_wait(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/div/div[2]/div[2]')
        # while True:
        thanks.click()
        # //*[@id="app"]/div/div/div[3]/div[2]/div/div[2]/div[2]
        time.sleep(0.5)

        con = smart_wait(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[1]/div[9]/div')
        con.click()

        time.sleep(0.5)
    else:
        slot.click()

    no = smart_wait(By.XPATH, '//*[@id="body"]/div[3]/form/div[2]/div/div[2]/div[3]')
    no.click()


def feed():
    # 57 secs
    # //*[@id="customer"]/div[3] -> customer
    # "plate1" -> food id
    # //*[@id="customer"]/div[3]
    time.sleep(0.5)
    for i in range(3):
        food = smart_wait(By.ID, 'plate1')
        food.click()

        customers = driver.find_elements(By.XPATH, '//*[@id="customer"]/div[3]') #//*[@id="customer"]/div[3]
        for customer in customers:
            try:
                customer.click()
            except:
                pass
        time.sleep(0.25)

def cafe():
    questions = 400
    start()
    beginning = int(time.time())

    while questions > 0:
        if (int(time.time()) - beginning)%5 == 0 and int(time.time()) != beginning:
            feed()
        try:
            restock = smart_wait(By.ID, 'restock')
            restock.click()

            time.sleep(0.5)
            question = smart_wait(By.ID, f'answer{random.randint(0,3)}')
            question.click()
            print("clicked question", questions)

            time.sleep(0.5)

            green = smart_wait(By.XPATH, '//*[@id="feedbackButton"]')
            green.click()
            questions -= 1
        except:
            upgrade = smart_wait(By.CLASS_NAME, 'styles__reportShopButton___2AvJR-camelCase')
            upgrade.click()

            time.sleep(0.5)

            next = smart_wait(By.ID, 'shopButton')
            next.click()
login()
cafe()
