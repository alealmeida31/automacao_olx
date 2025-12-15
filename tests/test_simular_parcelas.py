import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TESTE 1 — Deve encontrar HB20 S e clicar em simular parcelas validando se existe o texto "Parcelas"
def test_simular_parcelas(driver):
    wait = WebDriverWait(driver, 20)
    # Tentar localizar o ícone/botão inicial do app usando vários seletores
    el1 = None
    locators = [
        (AppiumBy.ACCESSIBILITY_ID, "OLX"),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("OLX")'),
        (AppiumBy.XPATH, "//*[contains(translate(@text,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'olx')]")
    ]
    for by, val in locators:
        try:
            el1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, val)))
            if el1:
                break
        except Exception:
            el1 = None

    if not el1:
        # diagnóstico: salvar page source e screenshot para investigação
        try:
            ps_path = 'debug_olx_page.xml'
            with open(ps_path, 'w', encoding='utf-8') as f:
                f.write(driver.page_source)
        except Exception:
            ps_path = None
        try:
            ss_path = 'debug_olx.png'
            driver.get_screenshot_as_file(ss_path)
        except Exception:
            ss_path = None
        msg = f"Não foi possível localizar o botão/ícone 'OLX'. page_source={ps_path} screenshot={ss_path}"
        pytest.fail(msg)

    el1.click()

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

    el6 = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 
        'new UiSelector().className("android.view.View").instance(8)'))
    )
    el6.click()

    el7 = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 
        'new UiSelector().text("Simular parcelas")'))
    )
    el7.click()

# VALIDAÇÃO: verificar se o texto "Entrada do financiamento" aparece na tela
    elemento_hb20 = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Entrada do financiamento")'))
    )

    # Faz o assert para garantir que o texto está lá
    assert "Entrada do financiamento" in elemento_hb20.text, "ERROR: O texto 'Entrada do financiamento' não foi encontrado na tela do anúncio!"

    print("✔ VALIDAÇÃO OK: Encontrado o texto Entrada do financiamento na simulação de financiamento")

# TESTE 2 — Deve encontrar HB20 S e clicar em simular parcelas e clicar em continuar
def test_simular_parcelas_continuar(driver):
    wait = WebDriverWait(driver, 20)
    # Tentar localizar o ícone/botão inicial do app usando vários seletores
    el1 = None
    locators = [
        (AppiumBy.ACCESSIBILITY_ID, "OLX"),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("OLX")'),
        (AppiumBy.XPATH, "//*[contains(translate(@text,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'olx')]")
    ]
    for by, val in locators:
        try:
            el1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, val)))
            if el1:
                break
        except Exception:
            el1 = None

    if not el1:
        # diagnóstico: salvar page source e screenshot para investigação
        try:
            ps_path = 'debug_olx_page.xml'
            with open(ps_path, 'w', encoding='utf-8') as f:
                f.write(driver.page_source)
        except Exception:
            ps_path = None
        try:
            ss_path = 'debug_olx.png'
            driver.get_screenshot_as_file(ss_path)
        except Exception:
            ss_path = None
        msg = f"Não foi possível localizar o botão/ícone 'OLX'. page_source={ps_path} screenshot={ss_path}"
        pytest.fail(msg)

    el1.click()

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

    el6 = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 
        'new UiSelector().className("android.view.View").instance(8)'))
    )
    el6.click()

    el7 = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 
        'new UiSelector().text("Simular parcelas")'))
    )
    el7.click()

    # Rola a tela até encontrar o botão "Continuar" usando UiScrollable.
    # Esta é uma forma mais robusta do que usar swipe com coordenadas fixas.
    continuar_selector = 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Continuar"))'
    el8 = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 
        continuar_selector))
    )
    el8.click()

    # VALIDAÇÃO 1: Verificar se o campo "Identificação" está visível
    identificacao_element = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Identificação")'))
    )
    assert identificacao_element.is_displayed(), "O campo 'Identificação' não está visível na tela."
    print("✔ VALIDAÇÃO OK: Campo 'Identificação' encontrado.")