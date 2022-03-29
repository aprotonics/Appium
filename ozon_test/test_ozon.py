from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


desired_caps = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "Pixel_5_API_30",
    "udid": "emulator-5554",
    "app": "/home/time-traveller/Desktop/Test_Frameworks/Appium/ozon_test/ozon_14.10-1941.apk"
}


class TestExample():
    def test_example(self):
        search_input_value = 'Shoes'
        
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps, strict_ssl=False)
        self.driver.implicitly_wait(10)

        # search
        search_input = self.driver.find_element(by=AppiumBy.ID, value='ru.ozon.app.android:id/searchTv')
        search_input.click()
        search_input_new = self.driver.find_element(by=AppiumBy.ID, value='ru.ozon.app.android:id/search_src_text')
        search_input_new.send_keys(search_input_value)
        self.driver.press_keycode(84)


        # click on product
        product_title = self.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@content-desc="tile-name"])[1]')
        product_title_value = product_title.text
        product_title.click()


        # add to card
        add_to_cart_button = self.driver.find_element(by=AppiumBy.ID, value='ru.ozon.app.android:id/mainBtn')
        add_to_cart_button.click()


        # go to card
        go_to_cart_button = self.driver.find_element(by=AppiumBy.ID, value='ru.ozon.app.android:id/menu_cart')
        go_to_cart_button.click()


        # check product title
        card_cart = self.driver.find_elements(by=AppiumBy.ACCESSIBILITY_ID, value='widget cart.cartSplit-1049434-default-1')[2]
        cart_product_title = card_cart.find_element(by=AppiumBy.XPATH, 
                            value='./androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.TextView')
        cart_product_title_value = cart_product_title.text


        assert cart_product_title_value == product_title_value, f'{cart_product_title_value} !== {product_title_value}'


        self.driver.quit()
