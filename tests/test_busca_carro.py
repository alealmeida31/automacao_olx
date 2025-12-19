import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# FIXTURE DO DRIVER
@pytest.fixture
def driver():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver

    # Finaliza app
    driver.terminate_app("com.schibsted.bomnegocio.androidApp")
    driver.quit()


# TESTE 1 — Deve encontrar HB20 S
def test_busca_hb20s(driver):
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

    # Aguarda carregamento das sugestões
    time.sleep(2)
    # Pressiona ENTER no teclado para buscar
    try:
        driver.execute_script('mobile: performEditorAction', {'action': 'search'})
    except Exception:
        driver.press_keycode(66)

    el5 = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("hb20 s")'))
    )
    el5.click()

# VALIDAÇÃO: verificar se o texto "HB20 S" aparece na tela
    elemento_hb20 = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("hb20 s")'))
    )

    # Faz o assert para garantir que o texto está lá
    assert "hb20 s" in elemento_hb20.text.lower(), "ERROR: O texto 'HB20 S' não foi encontrado na tela do anúncio!"

    print("✔ VALIDAÇÃO OK: O anúncio contém o texto HB20 S")

# TESTE 2 — Busca por “Car Appium” deve retornar sem resultados

def test_busca_sem_resultado(driver):
    wait = WebDriverWait(driver, 20)

    el1 = wait.until(EC.presence_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, "OLX")
    ))
    el1.click()

    el2 = wait.until(EC.presence_of_element_located(
        (AppiumBy.ANDROID_UIAUTOMATOR,
         'new UiSelector().className("android.view.View").instance(13)')
    ))
    el2.click()

    el3 = wait.until(EC.presence_of_element_located(
        (AppiumBy.CLASS_NAME, "android.widget.EditText")
    ))
    el3.click()
    el3.send_keys("Car Appium")

    # Tenta submeter/confirmar a busca — clicar em um item sugestão ou botão se existir
    try:
        el4 = wait.until(EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR,
             'new UiSelector().className("android.view.View").instance(8)')
        ))
        el4.click()
    except Exception:
        # se não houver esse botão, segue adiante
        pass

    # pequena espera para resultados aparecerem
    time.sleep(2)

    # Simples verificação: não deve haver nenhum TextView contendo o texto da busca
    search_lower = 'Car Appium'
    matches = driver.find_elements(
        AppiumBy.XPATH,
        "//android.widget.TextView[contains(translate(@text,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), 'car appium')]")

    if matches:
        # coleta textos para ajuda no debug
        texts = []
        for m in matches:
            try:
                texts.append(m.get_attribute('text') or m.get_attribute('content-desc') or '<sem texto>')
            except Exception:
                texts.append('<erro ao ler>')
        raise AssertionError(f"❌ A busca retornou resultados inesperados: {texts}")

    print("✔️ Resultado OK — Nenhum item encontrado para 'Car Appium'.")
