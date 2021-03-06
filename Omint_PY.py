import random
from idlelib import browser
from selenium import webdriver
import unittest
import time
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Omint(unittest.TestCase):
    def setUp(self):
        self.drive = webdriver.Chrome(r'C:\Users\Mañana\Documents\Automation\Browser\chromedriver.exe')
        self.drive.get('https://oaapp.eastus2.cloudapp.azure.com:8600/')
        self.drive.maximize_window()

    def test_cartilla(self):
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
        btn_clinica = self.drive.find_element_by_xpath( '/html/body/div[1]/div/main/div[1]/div/form/div[2]/div[1]/div/div[1]/div[1]')
        btn_clinica.click()
        clinica_elegir = self.drive.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div/form/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/span')
        clinica_elegir.click()
        time.sleep(1)
        boton_donde = self.drive.find_element_by_xpath('//*[@id="locality"]/div/div[1]')
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

    def test_generar_autorizacion(self):
        self.drive.find_element_by_xpath('//*[@id="dni"]').send_keys('49709124')
        time.sleep(1)
        self.drive.find_element_by_xpath('//*[@id="user"]').send_keys('prueba123')
        time.sleep(1)
        self.drive.find_element_by_xpath('//*[@id="password"]').send_keys('p12345')
        time.sleep(1)
        self.drive.find_element_by_xpath('//*[@id="root"]/div/div/div/form/button').click()
        time.sleep(3)
        solicitud = self.drive.find_element_by_xpath('//*[@id="root"]/div/header/div/div[1]/div[3]')
        autorizacion = self.drive.find_element_by_xpath('//*[@id="root"]/div/header/div/div[1]/div[3]/div/div[1]/a')
        action = ActionChains(self.drive)
        action.move_to_element(solicitud)
        time.sleep(3)
        action.click(autorizacion)
        action.perform()
        time.sleep(3)
        generar_autorizacion = self.drive.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[2]/div/div/a')
        generar_autorizacion.click()
        time.sleep(3)
        seleccionar = self.drive.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[3]/form/div/div/div/div[1]')
        seleccionar.click()
        time.sleep(2)
        nombre_elegir = self.drive.find_element_by_xpath('//*[@id="beneficiary"]/div/div[1]/div[1]/span')
        nombre_elegir.click()
        time.sleep(2)
        siguiente = self.drive.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[3]/form/button')
        siguiente.click()
        time.sleep(5)
        elegir_tratamiento = self.drive.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[3]/form/div/div/div[1]/div[1]')
        elegir_tratamiento.click()
        time.sleep(2)
        seleccionar_tratamiento = self.drive.find_element_by_xpath('// *[ @ id = "react-select-4-option-0-0"]')
        seleccionar_tratamiento.click()
        time.sleep(2)
        avanzar = self.drive.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[3]/form/button')
        avanzar.click()
        time.sleep(5)
        elegir_localidad = self.drive.find_element_by_xpath('//*[@id="locality"]/div/div[1]')
        elegir_localidad.click()
        time.sleep(2)
        seleccionar_localidad = self.drive.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[3]/form/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div/span').click()
        time.sleep(15)
        elegir_lugar = self.drive.find_element_by_xpath('//*[@id="place"]/div/div[1]/div[1]').click()
        time.sleep(2)
        opcion = self.drive.find_element_by_xpath('//*[@id="react-select-6-option-0"]').click()
        time.sleep(2)
        nombre_clinica = self.drive.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[3]/div/dialog/form/div[1]/div/input')
        print("hasta aca funca")
        print(nombre_clinica.is_enabled())
        nombre_clinica.send_keys('Bazterrica')
        time.sleep(2)
        btn_siguiente = self.drive.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[3]/div/dialog/form/div[3]/button[2]')
        btn_siguiente.click()
        time.sleep(1)
        fecha = self.drive.find_element_by_xpath('//*[@id="date"]').send_keys('06022020')
        time.sleep(2)
        comentarios = self.drive.find_element_by_xpath('//*[@id="observations"]').send_keys('esta es una prueba automatizada')
        time.sleep(2)
        subir = self.drive.find_element_by_id('file').send_keys(r'C:\Users\Mañana\Desktop\omint.jpg')
        time.sleep(5)
        finalizar_consulta = self.drive.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[3]/form/button')
        finalizar_consulta.click()
        time.sleep(5)
        btn_perfil = self.drive.find_element_by_xpath('//*[@id="root"]/div/header/div/div[1]/div[4]')
        btn_salir = self.drive.find_element_by_xpath('//*[@id="root"]/div/header/div/div[1]/div[4]/div/div[1]/button')
        action = ActionChains(self.drive)
        action.move_to_element(btn_perfil)
        time.sleep(1)
        action.click(btn_salir)
        action.perform()

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

    def test_crear_cuenta(self):
        self.drive.find_element_by_xpath('//*[@id="root"]/div/div/div/form/div[2]/a[1]').click()
        time.sleep(1)
        self.drive.find_element_by_xpath('//*[@id="cardNumber"]').send_keys('4694750902013')
        self.drive.find_element_by_xpath('//*[@id="birthDate"]').send_keys('03032002')
        self.drive.find_element_by_xpath('//*[@id="dni"]').send_keys('43819228')
        self.drive.find_element_by_xpath('//*[@id="email"]').send_keys('testingarbusta2@gmail.com ')
        self.drive.find_element_by_xpath('//*[@id="familyMemberCount"]').send_keys(random.randint(1, 8))
        self.drive.find_element_by_xpath('//*[@id="newUser"]').send_keys('Arbusta2017')
        self.drive.find_element_by_xpath('//*[@id="newPassword"]').send_keys('Arbusta2017')
        self.drive.find_element_by_xpath('//*[@id="newPasswordRepeat"]').send_keys('Arbusta2017')
        self.drive.find_element_by_xpath('//*[@id="root"]/div/div/div/form/button').click()
        time.sleep(1)
        self.drive.find_element_by_xpath('//*[@id="root"]/div[1]/dialog/div[2]/button').click()
        time.sleep(2)

    def tearDown(self):
        self.drive.quit()
