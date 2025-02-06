import os
from datetime import datetime

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import BASE_DIR
from utils.log import logger


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 打开浏览器
    def open_browser(self, url):
        logger.info('正在打开浏览器')
        self.driver.get(url)
        self.driver.maximize_window()

    # 查找元素(元素可见)
    def find_element(self, locator):
        logger.info('正在查找元素：{}'.format(locator))
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    # 点击
    def click(self, locator):
        logger.info('正在点击元素：{}'.format(locator))
        self.find_element(locator).click()

    # 输入
    def input(self, locator, text):
        logger.info('正在输入：{}'.format(text))
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    # 获取文本
    def get_text(self, locator):
        logger.info('正在获取文本')
        return self.find_element(locator).text

    # 切换frame
    def switch_frame(self, locator):
        logger.info('正在切换frame')
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(locator))

    # 换回主frame
    def switch_default_content(self):
        logger.info('正在切换回主frame')
        self.driver.switch_to.default_content()

    # 截图
    def screenshot(self, name=None):
        logger.info('正在截图')
        screenshot_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'screenshot')
        os.makedirs(screenshot_dir, exist_ok=True)
        if name is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
        else:
            filename = f"{name}.png"
        screenshot_path = os.path.join(screenshot_dir, filename)
        self.driver.save_screenshot(screenshot_path)