from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.wikipedia.org/")

# driver.page_source # can retrieve entire website 

# identify the id, name, or class (most useful to least)

# this is to use the search bar 
search = driver.find_element(By.ID, "searchInput") # access search
search.send_keys("chips") # search for this
search.send_keys(Keys.RETURN) # enter to search

try:
    # this is the main section
    section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mw-content-text"))
    )
    # this is for the subsections
    h2 = section.find_element(By.TAG_NAME, "h2")
    # if need to find tag within the subsection
    for h in h2:
        header = h2.find_element(By.ID, "ID")
        print(header.text)
except:
    driver.quit()


driver.close() # close the tab
driver.quit() # close browser
driver.title
