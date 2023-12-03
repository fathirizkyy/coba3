import pytest
from .conftest import setupNya
from .loginPage import testLogin


@pytest.mark.usefixtures("setupNya")
class TestLogin:
    def test_berhasil(self, setupNya):
        driver = testLogin(setupNya)
        setupNya.get("https://www.saucedemo.com/")
        driver.masukanUsername("standard_user")
        driver.masukanPassword("secret_sauce")
        driver.button()
        assert driver.infoSukses().text in "Products"

    def test_gagal(self, setupNya):
        driver = testLogin(setupNya)
        setupNya.get("https://www.saucedemo.com/")
        driver.masukanUsername("standard_user")
        driver.masukanPassword("secret")
        driver.button()
        assert driver.infGagal().text in "Epic sadface: Username and password do not match any user in this service"

