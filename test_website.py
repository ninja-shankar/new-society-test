import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

class NewSocietyTest(unittest.TestCase):
    """Test suite for New Society website"""

    def setUp(self):
        """Set up the test environment"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
        # Use file:// protocol to open the local HTML file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.html_path = os.path.join(current_dir, 'index.html')
        self.driver.get(f"file://{self.html_path}")
        
        # Give the page a moment to load
        time.sleep(1)

    def tearDown(self):
        """Clean up after the test"""
        self.driver.quit()

    def test_page_title(self):
        """Test if the page title is correct"""
        self.assertEqual(self.driver.title, "New Society")

    def test_header_content(self):
        """Test if the header contains the correct text"""
        header = self.driver.find_element(By.TAG_NAME, "header")
        header_text = header.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(header_text, "Welcome to New Society")

    def test_about_section(self):
        """Test if the About Us section exists and has content"""
        about_heading = self.driver.find_element(By.XPATH, "//h2[text()='About Us']")
        self.assertTrue(about_heading.is_displayed())
        
        # Check if the paragraphs exist
        paragraphs = self.driver.find_elements(By.XPATH, "//h2[text()='About Us']/following-sibling::p")
        self.assertGreaterEqual(len(paragraphs), 2)
        
        # Check content of the first paragraph
        self.assertIn("forward-thinking organization", paragraphs[0].text)

    def test_subscription_form(self):
        """Test if the subscription form exists and is functional"""
        # Check if the form exists
        form = self.driver.find_element(By.TAG_NAME, "form")
        self.assertTrue(form.is_displayed())
        
        # Check if the email input field exists
        email_input = self.driver.find_element(By.ID, "email")
        self.assertTrue(email_input.is_displayed())
        
        # Check if the subscribe button exists
        subscribe_button = self.driver.find_element(By.CLASS_NAME, "btn")
        self.assertTrue(subscribe_button.is_displayed())
        self.assertEqual(subscribe_button.text, "Subscribe")
        
        # Test form submission with dummy data
        email_input.send_keys("test@example.com")
        # We won't actually submit the form since there's no backend

    def test_footer_content(self):
        """Test if the footer contains the copyright information"""
        footer = self.driver.find_element(By.CLASS_NAME, "footer")
        self.assertTrue(footer.is_displayed())
        self.assertIn("2025 New Society", footer.text)

if __name__ == "__main__":
    unittest.main()