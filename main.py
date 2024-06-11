from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

webdriver_path = "chromedriver.exe"

options = Options()
options.headless = False

service = Service(webdriver_path)

driver = webdriver.Chrome(service=service, options=options)

url = "https://yandex.ru/maps/10295/kostanai/routes/bus_8/796d617073626d313a2f2f7472616e7369742f6c696e653f69643d31373034383931313134266c6c3d36332e36333735353625324335332e323630333939266e616d653d3826723d3537343626747970653d627573/?ll=63.638509%2C53.243958&tab=stops&z=12.14"

driver.get(url)

try:
    stops = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "masstransit-legend-group-view__item-link"))
    )

    print("Список остановок:")
    for stop in stops:
        stop_title = stop.get_attribute("title")
        stop_link = stop.get_attribute("href")
        print(f"{stop_title}: {stop_link}")

except StaleElementReferenceException:
    stops = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "masstransit-legend-group-view__item-link"))
    )

    print("Список остановок:")
    for stop in stops:
        stop_title = stop.get_attribute("title")
        stop_link = stop.get_attribute("href")
        print(f"{stop_title}: {stop_link}")

except Exception as e:
    print("Произошла ошибка:", e)

driver.quit()
