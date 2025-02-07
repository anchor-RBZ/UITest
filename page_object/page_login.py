from selenium.webdriver.common.by import By

from page_object.base import Base


class LoginPage(Base):
    def login(self, username, password):
        self.input((By.NAME, 'username'), username)
        self.input((By.NAME, 'password'), password)
        self.click((By.XPATH, "//span[contains(text(),'管理员')]"))
        self.click((By.CSS_SELECTOR, "button[type='button'] span"))

    # 获取登录信息
    def get_login_info(self):
        return self.get_text((By.XPATH, "//div[@class='user-info']"))

    # 获取错误信息
    def get_error_info(self):
        return self.get_alert_text()

    # 退出登录
    def logout(self):
        self.click((By.CLASS_NAME, "logout"))
