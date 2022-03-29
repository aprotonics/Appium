from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "11",
    "appium:deviceName": "Pixel_5_API_30",
    "appium:udid": "emulator-5554",
    "appium:appPackage": "com.wildberries.ru",
    "appium:appWaitActivity": "com.wildberries.ru.CountryListActivity",
    "appium:app": "/home/time-traveller/Desktop/Test_Frameworks/Appium/wildberries_test/com.wildberries.ru_4.5.5000.apk"
}

class TestExample():
    def test_example(self):
        search_input_value = 'hatber'
        
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps, strict_ssl=False)
        self.driver.implicitly_wait(10)

        actions = TouchAction(self.driver)

        # choose region
        region_items_checkboxes = self.driver.find_elements(by=AppiumBy.ID, value='com.wildberries.ru:id/checkbox')
        region_item_checkbox = region_items_checkboxes[0]
        actions.tap(region_item_checkbox).perform()

        # skip promo
        skip_button = self.driver.find_element(by=AppiumBy.ID, value='com.wildberries.ru:id/skip')
        actions.tap(skip_button).perform()

        # search
        search_input = self.driver.find_element(by=AppiumBy.ID, value='com.wildberries.ru:id/search_searchEditText')
        actions.tap(search_input).perform()
        search_input_new = self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText')
        search_input_new.send_keys(search_input_value)

        empty_field = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView/android.widget.ImageView')
        actions.tap(empty_field).perform()

        first_search_item = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]')
        actions.tap(first_search_item).perform()

        # click on product
        product_title = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='com.wildberries.ru:id/brandTitle')
        product_title_value = product_title.text
        actions.tap(product_title).perform()

        # add to card
        product_article = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='com.wildberries.ru:id/articleValue')
        product_article_value = product_article.text
        add_to_cart_button = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View')
        actions.tap(add_to_cart_button).perform()

        # go to card
        go_to_cart_button = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='com.wildberries.ru:id/btnBasket')
        actions.tap(go_to_cart_button).perform()

        # check product article
        cart_product_article = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='com.wildberries.ru:id/productArticleValue')
        cart_product_article_value = cart_product_article.text

        assert cart_product_article_value == product_article_value, f'{cart_product_article_value} !== {product_article_value}'

        self.driver.quit()
