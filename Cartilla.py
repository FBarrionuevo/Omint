from idlelib import browser

from selenium import webdriver
import unittest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Omint(unittest.TestCase):
    def setUp(self):
        self.drive = webdriver.Chrome(r'C:\Users\Mañana\Documents\Automation\Browser\chromedriver.exe')
        self.drive.get('https://oaapp.eastus2.cloudapp.azure.com:8600/')
            self.drive.maximize_window()

    def test_inicio(self):
        self.drive.find_element_by_xpath('//*[@id="dni"]').send_keys('49709124')
        time.sleep(1)
        self.drive.find_element_by_xpath('//*[@id="user"]').send_keys('prueba123')
        time.sleep(1)
        self.drive.find_element_by_xpath('//*[@id="password"]').send_keys('p12345')
        time.sleep(1)
        self.drive.find_element_by_xpath('//*[@id="root"]/div/div/div/form/button').click()
        time.sleep(3)
        btn_cartilla = self.drive.find_element_by_xpath('//*[@id="root"]/div/header/div/div[1]/div[2]/a')
        btn_cartilla.click()
        time.sleep(2)
        btn_clinica = self.drive.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div/form/div[2]/div[1]/div/div[1]/div[1]')
        btn_clinica.click()
        clinica_elegir = self.drive.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div/form/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/span')
        clinica_elegir.click()
        time.sleep(1)
        boton_donde = self.drive.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div/form/div[2]/div[2]/div/div[1]/div[1]')
        boton_donde.click()
        boton_selec_donde = self.drive.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div/form/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/span')
        boton_selec_donde.click()
        time.sleep(2)
        btn_buscar = self.drive.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div/form/div[3]/button[1]')
        btn_buscar.click()
        time.sleep(2)
        mapa = self.drive.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div[1]/div[2]/a/img')
        mapa.click()
        time.sleep(2)
        windows_before = self.drive.window_handles[0]
        windows_after = self.drive.window_handles[1]
        self.drive.switch_to_window(windows_after)
        time.sleep(5)
        self.drive.switch_to_window(windows_before)
        time.sleep(2)
        btn_perfil = self.drive.find_element_by_xpath('//*[@id="root"]/div/header/div/div[1]/div[4]')
        btn_salir = self.drive.find_element_by_xpath('/html/body/div/div/header/div/div[1]/div[4]/div/div[1]/button')
        action = ActionChains(self.drive)
        action.move_to_element(btn_perfil)
        time.sleep(1)
        action.click(btn_salir)
        action.perform()
        print('esto si funca')
        time.sleep(2)
        
    def tearDown(self):
        self.drive.quit()