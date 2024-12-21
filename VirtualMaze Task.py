import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service()  # Automatically downloads and manages ChromeDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://tracker.vmmaps.com/")
driver.maximize_window()
time.sleep(3)

#Click login Button:
driver.find_element(By.XPATH, "//a[text()='Login']").click()
time.sleep(1)
driver.find_element(By.ID, "email" ).send_keys("yogeships143@gmail.com")
time.sleep(1)
driver.find_element(By.ID,"pass").send_keys("Yogesh@Maps22")
time.sleep(1)
driver.find_element(By.ID,"loginSubmit").click()
time.sleep(1)
#Adding GPS Divice
driver.find_element(By.XPATH, "//p[text()='GPS Devices']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//p[text()='Add Device']").click()
time.sleep(1)
driver.find_element(By.ID, "imei-inputFieldBox").send_keys("565656778881234")
driver.find_element(By.ID, "Devicename-inputFieldBox").send_keys("Macbook")
driver.find_element(By.ID,"Brandname-inputFieldBox").send_keys("Apple")
driver.find_element(By.ID, "VehicleModel-inputFieldBox").send_keys("2023")
driver.find_element(By.ID, "RegisterNo-inputFieldBox").send_keys("TQ22QQ3323")
driver.find_element(By.ID,"minMilege-inputFieldBox").send_keys("12")
driver.find_element(By.ID, "maxMilege-inputFieldBox").send_keys("15")
driver.find_element(By.ID,"maxAllowedSpeed-inputFieldBox").send_keys("80")
driver.find_element(By.XPATH, "//p[text()='Submit']").click()
time.sleep(5)
#Creating Groups
driver.find_element(By.XPATH,"//p[text()='Groups']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//p[text()='New Group']").click()
driver.find_element(By.ID,"Groupname-inputFieldBox" ).send_keys("Testing1")
driver.find_element(By.ID,"GroupDes-inputFieldBox").send_keys("Python Testing new")
driver.find_element(By.CLASS_NAME,"DeviceListItem-box ").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//div[@class='select-indicator'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//p[text()='Create Group'])[2]").click()
time.sleep(2)
#Adding Geofences for Devices
driver.find_element(By.XPATH, "//p[text()='Geo Fencing']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Add']").click()
time.sleep(1)
#Viewing Reports
driver.find_element(By.XPATH,"//p[text()='Reports']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//img[@alt='dropdown icon']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//p[text()='Macbook']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='View Report']").click()
time.sleep(5)
#Live Tracking
driver.find_element(By.XPATH,"//p[text()='Live Tracking']").click()
time.sleep(1)
driver.find_element(By.ID,"livetrackingSearchInput").send_keys("iphone")
driver.find_element(By.ID,"livetrackingSearchInput").send_keys(Keys.ENTER)
time.sleep(5)

#Delete newly added GPS Device
driver.find_element(By.XPATH, "//p[text()='GPS Devices']").click()
time.sleep(1)
driver.find_element(By.XPATH,"(//div[@title='Delete'])[2]").click()
driver.find_element(By.XPATH, "//p[text()='Remove']").click()
time.sleep(3)
driver.close()