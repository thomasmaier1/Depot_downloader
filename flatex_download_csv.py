

def get_csv(save_location):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.firefox.options import Options
    import time

    # Setup download preferences
    # set profile to firefox webdriver
    profile = webdriver.FirefoxProfile()
    # disable file download to default folder
    profile.set_preference("browser.download.folderList", 2)
    # Disable showing the download process
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    # set desired download folder
    # profile.set_preference("browser.download.dir", "C:\Development\Python\Webdriver_test\download")
    profile.set_preference("browser.download.dir", save_location)
    # disable "save to disk" prompt
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

    # define webdriver
    driver = webdriver.Firefox(profile)
    time.sleep(1)   # Wait for 1 second (safety)

    try:
        # Open webpage
        driver.get("https://konto.flatex.at/banking-flatex.at/accountOverviewFormAction.do")

        # Find (+ wait for) and accept cookie popup button
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sg-cookie-optin-box-button-accept-all"))).click()
        print("cookie done")

        time.sleep(2)   # Wait for 1 second (safety)

        # Find (+ wait for) and open/click wrapper
        driver.find_element(By.CSS_SELECTOR, ".toggleWrapper").click()
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".toggleWrapper"))).click()
        print("wrapper done")

        time.sleep(1)   # Wait for 1 second (safety)

        # Find and fill in login&password
        user = driver.find_element(By.CSS_SELECTOR, "#uname_app")
        password = driver.find_element(By.CSS_SELECTOR, "#password_app")
        user.send_keys("xxx")
        password.send_keys("xxx")
        print("keys done")

        # Find (+ wait for) and click Login button (for some reason this has to be done 2 times)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button"))).click()
        print("login done")

        # 1. Minimize first window 2. Switch to new Depot window 3. Minimize depot window
        driver.minimize_window()
        driver.switch_to.window(driver.window_handles[1])
        driver.minimize_window()
        print("window_switch done")

        time.sleep(2)   # Wait for 1 second (safety)

        # Find and click combobox
        driver.find_element(By.ID, "depositStatementForm_tableActionCombobox").click()
        print("found combobox")

        time.sleep(1)   # Wait for 1 second (safety)

        # Find and click "CSV Download" selection
        driver.find_element(By.ID, "depositStatementForm_tableActionCombobox_entriesI1I").click()
        print("clicked csv download")

        time.sleep(1)   # Wait for 1 second (safety)

        # Close browser
        driver.quit()
        print("script done!")
        return 1

    except:
        print("script error")
        return 0

# value = get_csv()
# print(value)
