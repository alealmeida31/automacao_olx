# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

wait = WebDriverWait(driver, 20)

# Aguarda o elemento pelo accessibility id
el1 = wait.until(
    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "OLX"))
)
el1.click()

# Aguarda o próximo elemento
el2 = wait.until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().className("android.view.View").instance(13)'))
)
el2.click()

# Aguarda o campo de texto
el3 = wait.until(
    EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
)
el3.click()
el3.send_keys("hb20 s")

# Aguarda o botão ou item da lista
el4 = wait.until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().className("android.view.View").instance(8)'))
)
el4.click()

el5 = wait.until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().className("android.view.View").instance(6)'))
)
el5.click()

# ------------------------------------------
# ✅ VALIDAÇÃO: verificar se o texto "HB20 S" aparece na tela
# ------------------------------------------

elemento_hb20 = wait.until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().textContains("HB20 S")'))
)

# Faz o assert para garantir que o texto está lá
assert "HB20 S" in elemento_hb20.text, "ERROR: O texto 'HB20 S' não foi encontrado na tela do anúncio!"

print("✔ VALIDAÇÃO OK: O anúncio contém o texto HB20 S")

driver.terminate_app("com.schibsted.bomnegocio.androidApp")

driver.quit()


