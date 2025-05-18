from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_image(self):
        image_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@class, 'image-gallery-image')]"))
        )
        return image_element.get_attribute("src")

    def get_product_name(self):
        name_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'chakra-heading')]"))
        )
        return name_element.text

    def get_product_description(self):
        description_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'chakra-card__body')]/p[contains(text(), 'Description')]"))
        )
        return description_element.text

    def get_product_price(self):
        price_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'chakra-card__body')]/p[contains(text(), '$')]"))
        )
        return price_element.text

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/signin']"))
        )
        login_button.click()

    def click_register_button(self):
        register_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/signup']"))
        )
        register_button.click()

    def click_add_to_bag_button(self):
        add_to_bag_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Add to Cart') or contains(text(), 'Add to Bag')]"))
        )
        add_to_bag_button.click()
