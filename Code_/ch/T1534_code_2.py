from selenium import webdriver

def send_internal_spearphishing_email(from_email, to_email, subject, body):
    driver = webdriver.Chrome('path_to_chrome_driver')
    driver.get('https://your_email_provider.com')
    # 登入郵件帳號
    # ...

    # 進入撰寫郵件頁面
    # ...

    # 填寫郵件內容
    # ...
    driver.find_element_by_id('subject').send_keys(subject)
    driver.find_element_by_id('body').send_keys(body)
    driver.find_element_by_id('recipient').send_keys(to_email)

    # 發送郵件
    # ...
    driver.find_element_by_id('send_button').click()

    driver.quit()
    print('Internal spearphishing email sent successfully.')

# 使用方法
send_internal_spearphishing_email('from@example.com', 'to@example.com', 'Important Notice', 'Please update your account password by clicking on the link: http://example.com')