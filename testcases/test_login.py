import pytest

from page_object.page_login import LoginPage


class TestLogin:

    @pytest.mark.parametrize('username, password, info',
                             [('admin', '123456', '管理员 admin'),
                              ('admin', '1234', '账号或密码不正确')],
                             ids=['successful', 'pwd_error'])
    def test_login(self, username, password, info, login_page):
        login_page.login(username, password)
        if info == '管理员 admin':
            assert login_page.get_login_info() == info
            login_page.logout()
        else:
            assert login_page.get_error_info() == info
