from selenium import webdriver
import time 

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Bom dia!"
        self.grupos = ["Eu msm"]
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    
    def EnviarMensagens(self):
     # <span dir="auto" title="Eu msm" class="_3ko75 _5h6Y_ _3Whw5">Eu msm</span>
     # <div tabindex="-1" class="_3uMse"></div>
     # <span data-testid="send" data-icon="send" class=""></span>
     print('Desenvolvimento')
     self.driver.get('https://ww.web.whatsapp.com')
     time.sleep(30)
     for grupo in self.grupos:
         grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
         time.sleep(3)
         grupo.click()
         chat_box = self.driver.find_element_by_class_name('_3uMse')
         time.sleep(3)
         chat_box.click()
         chat_box.send_keys(self.mensagem)
         button_send = self.driver.find_element_by_xpath("//span[@data-icon='send']")
         time.sleep(3)
         button_send.click()
         time.sleep(5)
bot = WhatsappBot()
bot = EnviarMensagens()