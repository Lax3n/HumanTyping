from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os

# Add parent directory to path to import src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from humantyping.integration import HumanTyper

def main():
    print("Launching Chrome...")
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://www.google.com")
        print("Navigating to google.com...")
        
        # Create HumanTyper
        human = HumanTyper(wpm=65)
        
        # Find search box
        search_box = driver.find_element(By.NAME, "q")
        print("Typing...")
        
        # Type realistically
        human.type_sync(search_box, "Selenium with human typing")
        
        print(f"Typed value: {search_box.get_attribute('value')}")
        print("Done.")
        
    finally:
        input("Press Enter to close browser...")
        driver.quit()

if __name__ == "__main__":
    main()
