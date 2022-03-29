from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


# adb shell pm list packages
# adb shell dumpsys activity | grep 'mCurrent'

desired_caps = {
    "platformName": "Android",
    "platformVersion": "8.0.0",
    "deviceName": "Pixel_2_API_26",
    "udid": "emulator-5554",
    "app": "./eribank.apk"
}


class TestExample():
    def test_example(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps, strict_ssl=False)
        self.driver.implicitly_wait(10)

        username_input = self.driver.find_element(by=AppiumBy.ID, value='com.experitest.ExperiBank:id/usernameTextField')
        username_input.send_keys('username')

        password_input = self.driver.find_element(by=AppiumBy.ID, value='com.experitest.ExperiBank:id/passwordTextField')
        password_input.send_keys('password')

        submit_button = self.driver.find_element(by=AppiumBy.ID, value='com.experitest.ExperiBank:id/loginButton')
        submit_button.click()

        error_text_element = self.driver.find_element(by=AppiumBy.ID, value='android:id/message')
        error_text = error_text_element.text
        
        assert error_text == 'Invalid username or password!'

        self.driver.quit()
