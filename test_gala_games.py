from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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
        self.chrome_driver.implicitly_wait(10)
        self.chrome_wait = WebDriverWait(self.chrome_driver, 5)
        self.sleep_time = 2

    def accept_privacy_policy(self):
        self.chrome_wait.until(ec.presence_of_element_located((By.XPATH, '/html/body[@class="overflowHidden"]')))
        shadow_host = self.chrome_driver.find_element(By.ID, 'usercentrics-root')
        shadow_root = shadow_host.shadow_root
        shadow_root.find_element(By.CSS_SELECTOR, 'button[data-testid="uc-accept-all-button"]').click()

    def teardown_method(self):
        self.chrome_driver.close()
        self.chrome_driver.quit()

    def test_launch_town_star_not_logged_in(self):
        """From the Games page I should not be able to launch Town Star without being logged in"""
        self.chrome_driver.get("https://app.gala.games/games")

        self.accept_privacy_policy()

        play_element = self.chrome_wait.until(ec.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Play']")))
        play_element.click()

        form_element = self.chrome_wait.until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, 'form[novalidate="novalidate"]')))
        form_text = form_element.text

        assert form_text.startswith('Create your Account'), 'Account creation form not presented'

        sleep(self.sleep_time) # Pause for a moment to let video capture run.

    def test_store_search(self):
        """From the Store page Search for an item of your choice"""
        self.chrome_driver.get("https://app.gala.games/store")

        self.accept_privacy_policy()

        search_element = self.chrome_wait.until(ec.element_to_be_clickable(
            (By.XPATH, "//input[@type='text' and @placeholder='Search']")))
        search_element.click()
        search_element.send_keys("best friend")

        # TODO: Ideally there would be some form of validation here to use in an assert.

        sleep(self.sleep_time) # Give it some time to capture the video.

    def test_store_filter_town_star_epic_rarity(self):
        """From the Store page I should be able to filter Town Star items by Epic Rarity"""
        self.chrome_driver.get("https://app.gala.games/store")

        store_town_star_filter = 'https://app.gala.games/store?games=town-star'
        store_town_star_and_epic_rarity_filter = f'{store_town_star_filter}&rarity=epic'

        self.accept_privacy_policy()

        town_star_filter_element = self.chrome_wait.until(ec.element_to_be_clickable(
            (By.XPATH, "//img[@alt='Town Star']")))
        town_star_filter_element.click()
        self.chrome_wait.until(ec.url_to_be(store_town_star_filter))

        actual_url_1 = self.chrome_driver.current_url
        assert actual_url_1 == store_town_star_filter, f'actual_url_1 ({actual_url_1}) does not match expected_url_1 \
            ({store_town_star_filter})'

        epic_rarity_filter = self.chrome_wait.until(ec.element_to_be_clickable((By.XPATH, '//div[4]/div/i')))
        epic_rarity_filter.click()
        self.chrome_wait.until(ec.url_to_be(store_town_star_and_epic_rarity_filter))

        actual_url_2 = self.chrome_driver.current_url
        assert actual_url_2 == store_town_star_and_epic_rarity_filter, f'actual_url_2 ({actual_url_2}) does not match \
            expected_url_2 ({store_town_star_and_epic_rarity_filter})'

        sleep(self.sleep_time) # Give it some time to capture the video.

    def test_store_filter_spider_tanks_rare_rarity(self):
        """From the Store page I should be able to filter Spider Tank items by Rare Rarity"""
        self.chrome_driver.get("https://app.gala.games/store")

        store_spider_tanks_filter = 'https://app.gala.games/store?games=spider-tanks'
        store_spider_tanks_and_rare_rarity_filter = f'{store_spider_tanks_filter}&rarity=rare'

        self.accept_privacy_policy()

        spider_tanks_filter_element = self.chrome_wait.until(ec.element_to_be_clickable(
            (By.XPATH, "//img[@alt='Spider Tanks']")))
        spider_tanks_filter_element.click()
        self.chrome_wait.until(ec.url_to_be(store_spider_tanks_filter))

        actual_url_1 = self.chrome_driver.current_url
        assert actual_url_1 == store_spider_tanks_filter, f'actual_url_1 ({actual_url_1}) does not match \
            expected_url_1 ({store_spider_tanks_filter})'

        rare_rarity_filter = self.chrome_wait.until(ec.element_to_be_clickable((By.XPATH, '//div[3]/div/i')))
        rare_rarity_filter.click()
        self.chrome_wait.until(ec.url_to_be(store_spider_tanks_and_rare_rarity_filter))

        actual_url_2 = self.chrome_driver.current_url
        assert actual_url_2 == store_spider_tanks_and_rare_rarity_filter, f'actual_url_2 ({actual_url_2}) does not \
            match expected_url_2 ({store_spider_tanks_and_rare_rarity_filter})'

        sleep(self.sleep_time) # Give it some time to capture the video.
