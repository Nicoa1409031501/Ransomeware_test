from selenium import webdriver

def search_websites(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 在後台運行瀏覽器
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    titles = driver.find_elements_by_tag_name('title')
    titles = [title.get_attribute('textContent') for title in titles]
    driver.quit()
    return titles