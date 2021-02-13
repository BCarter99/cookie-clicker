from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


print('Press Ctrl-C to terminate at any time')


# declares path of the chromedriver, initializes driver, and opens the url of the cookie clicker website
PATH = "/home/brandon/Documents/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")


# allows the website to load before trying to find the elements
driver.implicitly_wait(10)


# locates and defines the cookie to click on, the number of cookies owned, and the upgrades
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id('productPrice' + str(i)) for i in range(1, -1, -1)]


actions = ActionChains(driver)
actions.double_click(cookie)


# runs the code unless user presses Ctrl-C
try:
    # clicks the big cookie while checking for available upgrades
    loop = True
    while loop:
        actions.perform()
        count = cookie_count.text.split(" ")[0]
        count = int(count.replace(",", ""))
        # checks to see if any upgrades are available, and clicks if yes
        for item in items:
            value = int(item.text)
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()

except KeyboardInterrupt:
    loop = False