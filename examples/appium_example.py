import os
import sys
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Add parent directory to path to import humantyping
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from humantyping.integration import HumanTyper


def main():
    """
    Example of using HumanTyping with Appium for native Android automation.
    This example automates the native Google Search app (QuickSearchBox).
    It avoids using Chromedriver by interacting with the native UI.
    """
    # Load Device UUID (UDID) from environment variable
    device_uuid = os.environ.get("APPIUM_DEVICE_UUID")

    if not device_uuid:
        print("⚠️ Warning: APPIUM_DEVICE_UUID environment variable not set.")
        print("Please set it: export APPIUM_DEVICE_UUID='your_device_udid'")

    print(f"Setting up Appium capabilities for Device: {device_uuid or 'Default'}")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    if device_uuid:
        options.udid = device_uuid

    # Automate the native Google App instead of Chrome browser
    options.app_package = "com.google.android.googlequicksearchbox"
    options.app_activity = "com.google.android.googlequicksearchbox.SearchActivity"
    options.no_reset = True

    print("Connecting to Appium server...")
    try:
        # Default Appium server URL is http://localhost:4723
        driver = webdriver.Remote("http://localhost:4723", options=options)
    except Exception as e:
        print(f"❌ Failed to connect to Appium server: {e}")
        return

    try:
        # Create HumanTyper
        human = HumanTyper(wpm=45)

        print("Waiting for Google Search to load...")
        time.sleep(2)

        # Finding the search box in the native Google App
        # Note: Resource IDs can vary slightly by Android version
        print("Finding native search field...")
        try:
            # Common ID for the search input in Google App
            search_button = driver.find_element(
                by=AppiumBy.XPATH,
                value='(//android.widget.FrameLayout[@resource-id="com.google.android.googlequicksearchbox:id/navigation_bar_item_icon_container"])[2]',
            )
            search_button.click()

            search_box = driver.find_element(
                by=AppiumBy.XPATH,
                value='//android.widget.EditText[@resource-id="com.google.android.googlequicksearchbox:id/googleapp_search_box"]',
            )
        except:
            # Fallback to a more generic search for an editable field
            print("ID search failed, looking for any focused edit text...")
            search_box = driver.switch_to.active_element

        print("Clicking search box...")
        search_box.click()

        # Type realistically using the synchronous integration
        print("Typing like a human on native Android app...")
        human.type_sync(search_box, "Human typing on native Android")

        print("✅ Finished typing.")
        time.sleep(2)

    except Exception as e:
        print(f"❌ Error during automation: {e}")
    finally:
        print("Closing session...")
        driver.quit()


if __name__ == "__main__":
    main()
