from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service('E:\Softs\chrome-win64\chromedriver.exe')
driver = webdriver.Chrome(service= ser)
driver.get('https://store.steampowered.com/')

# Maximizing Window
driver.maximize_window()


time.sleep(4)
# 'Action' Button
driver.find_element(by=By.XPATH,
                    value='//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div[2]/a[3]').click()
print('Action Buttion Done')

driver.execute_script("window.scrollTo(0, 1900);")

time.sleep(5)
# 'Top Sellers' Button
driver.find_element(by=By.XPATH,
                    value='//*[@id="SaleSection_13268"]/div[2]/div[2]/div[1]/div/div[3]').click()
print('Top Sellers Button Done')


# Scrolling to the middle of the page 
time.sleep(2)
driver.execute_script("window.scrollTo(0, 3350);")

time.sleep(2)
# Retreiveing old height 
old_height = driver.execute_script("return document.body.scrollHeight")
print('Old Height ',old_height)


time.sleep(5)
# Clicking 'Show More Button'
driver.find_element(by=By.CSS_SELECTOR,
                       value='#SaleSection_13268 > div._1cOoCFwafBlSkwllIMf3XM._39HWXhhjsbML7K9sme9ItV.SaleSectionForCustomCSS > div._18byEIHFiivSklOwKqIx2b > div:nth-child(2) > div._3vjDu6zylspBzUE7FmM6Yl > div > div._36qA-3ePJIusV1oKLQep-w > button').click()
print('Show More Button Done')

# Getting New Height
# time.sleep(2)
new_height = driver.execute_script('return document.body.scrollHeight')
print('New Height ',new_height)


time.sleep(2)
driver.execute_script("window.scrollTo(0, 5000);")

time.sleep(2)
item_no = 25
scroll_change = 6080

# when the old height is equal to new height , the loop will end
while old_height != new_height:

    # you can increase the time sleep seconds if the page takes time to load 
    try:
        time.sleep(.5)
        old_height = driver.execute_script('return document.body.scrollHeight')

        # Clicking the new Show More Button
        driver.find_element(by=By.CSS_SELECTOR,
                       value='#SaleSection_13268 > div._1cOoCFwafBlSkwllIMf3XM._39HWXhhjsbML7K9sme9ItV.SaleSectionForCustomCSS > div._18byEIHFiivSklOwKqIx2b > div:nth-child(2) > div._3vjDu6zylspBzUE7FmM6Yl > div > div._36qA-3ePJIusV1oKLQep-w > button').click()

        item_no += 12
        time.sleep(3)   
        driver.execute_script(f"window.scrollTo(0, {scroll_change});")
        scroll_change += 1200

        print('Extracted ',item_no,' Items')

        new_height = driver.execute_script('return document.body.scrollHeight')

    except:
        print('-'*50)
        print('Terminated at ',item_no)
        break
    
    

    
new_height = driver.execute_script('return document.body.scrollHeight')

print('Old Height ',old_height)
print('New Height ',new_height)

html = driver.page_source

with open('test_steam.html','w',encoding='utf-8' ) as file:
    file.write(html)

time.sleep(10)

driver.quit()