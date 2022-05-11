from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestGalaGames():
    def setup_method(self):
        # Set the base webdriver options.
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--browserTimeout 60')
        options.add_argument('--timeout 60')

        # Set the Video Recording webdriver options
        options.set_capability(name='browserName', value='chrome')
        options.set_capability(name='platformName', value='linux')
        options.set_capability(name='se:recordVideo', value='true')
        options.set_capability(name='se:timeZone', value='US/Pacific')
        options.set_capability(name='se:screenResolution', value='1920x1080')
        self.chrome_driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
        self.chrome_driver.maximize_window()
        self.vars = {}

    def teardown_method(self):
        self.chrome_driver.close()
        self.chrome_driver.quit()

    def test_launch_town_star_not_logged_in(self):
        """From the Games page I should not be able to launch Town Star without being logged in"""
        self.chrome_driver.get("https://app.gala.games/games")

        sleep(5) # TODO: Ugly but will suffice until I get a chance to look into WebDriverWait and expected_conditions

        # Accept the Privacy Policy
        # TODO: Turn this into a function/fixture.
        shadow_host = self.chrome_driver.find_element(By.ID, 'usercentrics-root')
        shadow_root = shadow_host.shadow_root
        shadow_root.find_element(By.CSS_SELECTOR, 'button[data-testid="uc-accept-all-button"]').click()

        sleep(5) # TODO: Ugly but will suffice until I get a chance to look into WebDriverWait and expected_conditions

        self.chrome_driver.find_element(By.XPATH, "//button[normalize-space()='Play']").click()

        sleep(5) # TODO: Ugly but will suffice until I get a chance to look into WebDriverWait and expected_conditions

        form_text = self.chrome_driver.find_element(By.CSS_SELECTOR, 'form[novalidate="novalidate"]').text
        assert form_text.startswith('Create your Account'), 'Account creation form not presented'

    def test_store_search(self):
        """From the Store page Search for an item of your choice"""
        self.chrome_driver.get("https://app.gala.games/store")

        sleep(5) # TODO: Ugly but will suffice until I get a chance to look into WebDriverWait and expected_conditions

        # Accept the Privacy Policy
        # TODO: Turn this into a function/fixture.
        shadow_host = self.chrome_driver.find_element(By.ID, 'usercentrics-root')
        shadow_root = shadow_host.shadow_root
        shadow_root.find_element(By.CSS_SELECTOR, 'button[data-testid="uc-accept-all-button"]').click()

        sleep(5) # TODO: Ugly but will suffice until I get a chance to look into WebDriverWait and expected_conditions

        self.chrome_driver.find_element(By.XPATH, "//input[@type='text']").click()
        self.chrome_driver.find_element(By.XPATH, "//input[@type='text']").send_keys("best friend")

        # TODO: Ideally there would be some form of validation here to use in an assert.

        sleep(5) # Give it some time to capture the video.

    def test_store_filter_by_towns_star_epic_rarity(self):
        """From the Store page I should be able to filter Town Star items by Epic Rarity"""
        self.chrome_driver.get("https://app.gala.games/store")

        sleep(5) # TODO: Ugly but will suffice until I get a chance to look into WebDriverWait and expected_conditions

        # Accept the Privacy Policy
        # TODO: Turn this into a function/fixture.
        shadow_host = self.chrome_driver.find_element(By.ID, 'usercentrics-root')
        shadow_root = shadow_host.shadow_root
        shadow_root.find_element(By.CSS_SELECTOR, 'button[data-testid="uc-accept-all-button"]').click()

        sleep(5) # TODO: Ugly but will suffice until I get a chance to look into WebDriverWait and expected_conditions

        self.chrome_driver.find_element(By.XPATH, "//img[@alt='Town Star']").click()
        self.chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[4]/div/i').click() # TODO: Find a better way to get to this element.

        # TODO: Ideally there would be some form of validation here to use in an assert.

        sleep(5)  # Give it some time to capture the video.

    def test_store_filter_by_spider_tanks_rare_rarity(self):
        """From the Store page I should be able to filter Spider Tank items by Rare Rarity"""
        self.chrome_driver.get("https://app.gala.games/store")

        sleep(5) # TODO: Ugly but will suffice until I get a chance to look into WebDriverWait and expected_conditions

        # Accept the Privacy Policy
        # TODO: Turn this into a function/fixture.
        shadow_host = self.chrome_driver.find_element(By.ID, 'usercentrics-root')
        shadow_root = shadow_host.shadow_root
        shadow_root.find_element(By.CSS_SELECTOR, 'button[data-testid="uc-accept-all-button"]').click()

        sleep(5) # TODO: Ugly but will suffice until I get a chance to look into WebDriverWait and expected_conditions

        self.chrome_driver.find_element(By.XPATH, "//img[@alt='Spider Tanks']").click()
        self.chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[3]/div/i').click() # TODO: Find a better way to get to this element.

        # TODO: Ideally there would be some form of validation here to use in an assert.

        sleep(5) # Give it some time to capture the video.
