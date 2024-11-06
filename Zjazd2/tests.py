from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from parameterized import parameterized

class TestWebApplications(unittest.TestCase):

    def setUp(self):
        self.driver = None

    def initialize_driver(self, browser):
        if browser == 'edge':
            self.driver = webdriver.Edge()
        elif browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser!")

    @parameterized.expand([
        ("edge",),
        ("chrome",),
        ("firefox",)
    ])
    def test_wikipedia_elements(self, browser):
        self.initialize_driver(browser)
        driver = self.driver
        driver.get("https://www.wikipedia.org")
        
        print(f"Title: {driver.title}")
        self.assertIn("Wikipedia", driver.title)
        
        logo = driver.find_element(By.CLASS_NAME, "central-featured-logo")
        print(f"Logo found: {logo is not None}")
        self.assertTrue(logo)
        
        search_input = driver.find_element(By.NAME, "search")
        print(f"Search input found: {search_input is not None}")
        self.assertTrue(search_input)
        
        search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        print(f"Search button found: {search_button is not None}")
        self.assertTrue(search_button)
        
        english_link = driver.find_element(By.ID, "js-link-box-en")
        print(f"English link found: {english_link is not None}")
        self.assertTrue(english_link)
        
        polish_link = driver.find_element(By.CSS_SELECTOR, "a[lang='pl']")
        print(f"Polish link found: {polish_link is not None}")
        self.assertTrue(polish_link)
        
        german_link = driver.find_element(By.CSS_SELECTOR, "a[lang='de']")
        print(f"German link found: {german_link is not None}")
        self.assertTrue(german_link)
        
        french_link = driver.find_element(By.CSS_SELECTOR, "a[lang='fr']")
        print(f"French link found: {french_link is not None}")
        self.assertTrue(french_link)
    
    @parameterized.expand([
        ("edge",),
        ("chrome",),
        ("firefox",)
    ])
    def test_stackoverflow_elements(self, browser):
        self.initialize_driver(browser)
        driver = self.driver
        driver.get("https://stackoverflow.com")
        
        print(f"Title: {driver.title}")
        self.assertIn("Stack Overflow", driver.title)
        
        login_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Log in')]")
        print(f"Log in button found: {login_button is not None}")
        self.assertTrue(login_button)
        
        search_input = driver.find_element(By.NAME, "q")
        print(f"Search input found: {search_input is not None}")
        self.assertTrue(search_input)
        
        search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        print(f"Search button found: {search_button is not None}")
        self.assertTrue(search_button)
        
        home_link = driver.find_element(By.XPATH, "//a[@href='/']")
        print(f"Home link found: {home_link is not None}")
        self.assertTrue(home_link)
        
        questions_link = driver.find_element(By.XPATH, "//a[@href='/questions']")
        print(f"Questions link found: {questions_link is not None}")
        self.assertTrue(questions_link)
        
        tags_link = driver.find_element(By.XPATH, "//a[@href='/tags']")
        print(f"Tags link found: {tags_link is not None}")
        self.assertTrue(tags_link)
        
        users_link = driver.find_element(By.XPATH, "//a[@href='/users']")
        print(f"Users link found: {users_link is not None}")
        self.assertTrue(users_link)
        
    @parameterized.expand([
        ("edge",),
        ("chrome",),
        ("firefox",)
    ])
    def test_github_elements(self, browser):
        self.initialize_driver(browser)
        driver = self.driver
        driver.get("https://github.com")
        
        print(f"Title: {driver.title}")
        self.assertIn("GitHub", driver.title)
        
        sign_in_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign in')]")
        print(f"Sign in button found: {sign_in_button is not None}")
        self.assertTrue(sign_in_button)
        
        sign_up_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign up')]")
        print(f"Sign up button found: {sign_up_button is not None}")
        self.assertTrue(sign_up_button)
        
        pricing_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Pricing')]")
        print(f"Pricing link found: {pricing_link is not None}")
        self.assertTrue(pricing_link)
        
        security_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Security')]")
        print(f"Security link found: {security_link is not None}")
        self.assertTrue(security_link)
        
        careers_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Careers')]")
        print(f"Careers link found: {careers_link is not None}")
        self.assertTrue(careers_link)
        
        features_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Features')]")
        print(f"Features link found: {features_link is not None}")
        self.assertTrue(features_link)
        
        enterprise_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Enterprise')]")
        print(f"Enterprise link found: {enterprise_link is not None}")
        self.assertTrue(enterprise_link)
    
    @parameterized.expand([
        ("edge",),
        ("chrome",),
        ("firefox",)
    ])
    def test_amazon_elements(self, browser):
        self.initialize_driver(browser)
        driver = self.driver
        driver.get("https://www.amazon.com")
        
        print(f"Title: {driver.title}")
        self.assertIn("Amazon.com. Spend less. Smile more.", driver.title)
        
        search_input = driver.find_element(By.ID, "twotabsearchtextbox")
        print(f"Search input found: {search_input is not None}")
        self.assertTrue(search_input)
        
        search_button = driver.find_element(By.ID, "nav-search-submit-button")
        print(f"Search button found: {search_button is not None}")
        self.assertTrue(search_button)
        
        home_link = driver.find_element(By.ID, "nav-logo-sprites")
        print(f"Home link found: {home_link is not None}")
        self.assertTrue(home_link)
        
        todays_deals_link = driver.find_element(By.XPATH, "//a[contains(text(), \"Today's Deals\")]")
        print(f"Today's Deals link found: {todays_deals_link is not None}")
        self.assertTrue(todays_deals_link)
        
        customer_service_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Customer Service')]")
        print(f"Customer Service link found: {customer_service_link is not None}")
        self.assertTrue(customer_service_link)
        
        registry_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Registry')]")
        print(f"Registry link found: {registry_link is not None}")
        self.assertTrue(registry_link)
        
        gift_cards_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Gift Cards')]")
        print(f"Gift Cards link found: {gift_cards_link is not None}")
        self.assertTrue(gift_cards_link)

        driver.quit()

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
