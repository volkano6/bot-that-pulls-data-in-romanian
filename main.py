import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.news.ro/"


def main():
    news = []
    sentence_count = 2000
    loop_is_continue = True
    page = 1

    driver.get(url)
    time.sleep(3)

    aaa = driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
    aaa.click()
    print("sekme kapandı")

    news_page = driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/div[1]/section/div/footer/a")
    news_page.click()
    print("haberlerin oldupu sayfaya gelindi")
    time.sleep(3)

    while loop_is_continue:
        news = driver.find_elements(By.CSS_SELECTOR, ".row.article")
        for new in range(len(news)):
            # time.sleep(3)
            # driver.find_element(By.XPATH, f"/html/body/div[7]/div/main/section/article[{new + 1}]/div[2]/h2/a").click()
            print(f"page: {new+1}")
            # time.sleep(3)
            # driver.back()

        driver.find_element(By.XPATH, "/html/body/div[7]/div/main/nav/ul/li[7]/a").click()
        time.sleep(4)

        if sentence_count == 3000:
            loop_is_continue = False

    driver.close()
    print("sayfa kapandı")


if __name__ == '__main__':
    main()
