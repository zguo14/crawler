import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class crowler(object):
    
    def rescheduleTest(self):
        self.url = "https://drivetest.ca/dtbookingngapp/registration/confirmRegistration"
        driver = uc.Chrome(user_subprocess=True)
        wait = WebDriverWait(driver, 20)
        driver.get(self.url)
        
        time.sleep(4)
        
        signInBtn = driver.find_element(By.XPATH, "//*[@id='booking-container']/div/div[2]/form/a")
        signInBtn.click()
        
        time.sleep(5)
        
        licenceNumber = wait.until(EC.element_to_be_clickable((By.ID, 'driverLicenceNumber')))
        expiryDate = wait.until(EC.element_to_be_clickable((By.ID, 'driverLicenceExpiry')))
        licenceNumber.send_keys(self.licenceNumber)
        expiryDate.send_keys(self.expiryDate)
        
        time.sleep(2)
        submitBtn = driver.find_element(By.XPATH, "//*[@id='componentID']/form/div[4]/app-progress-button/button")
        submitBtn.click()
        time.sleep(10)
        
        rescheduleBtn = driver.find_element(By.XPATH, "//*[@id='headingDiv']/div[3]/div/div/div[2]/div[3]/ul/li[2]/button")
        rescheduleBtn.click()
        time.sleep(5)
        
        cfmRescheduleBtn = driver.find_element(By.XPATH, "//*[@id='mat-dialog-0']/app-appt-modal/div[2]/div[2]/div[1]/app-progress-button/button")
        cfmRescheduleBtn.click()
        
        time.sleep(5)
        
        continueBtn = driver.find_element(By.XPATH, "//*[@id='main']/app-drivetest-locations/div/div/div[5]/app-progress-button/button")
        continueBtn.click()
        
        time.sleep(5)
        
        curDate = 111
        earliestDate = 111
        earliestDateXP = ""
        
        # calendar = driver.find_element(By.XPATH, "//*[@id='main']/app-select-date/div/app-calendar-selection-container")
        # //*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[4]
        # //*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[5]
        # print(calendar)
        
        for i in range(7, 9):
            # rows
            # xpath = "//*[@id='main']/app-select-date/div/app-calendar-selection-container/div[" + i + "]"
            # row = driver.find_element(By.XPATH, xpath)
            for k in range(1, 8):
                # //*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[6]/div[1]
                dxpath = "//*[@id='main']/app-select-date/div/app-calendar-selection-container/div[" + str(i) + "]/div[" + str(k) + "]"
                dxpath_btn = dxpath + "/app-date-selection/button"
                dxpath_btn_num = dxpath_btn + "/div"
                date_num = driver.find_element(By.XPATH, dxpath_btn_num)
                print(date_num.text)
                if date_num.text == "G2 @ 09:55 AM":
                    continue
                if int(date_num.text) < 26:
                    dateBtn = driver.find_element(By.XPATH, dxpath_btn)
                    dateBtn.click()
            
        continueBtn2 = driver.find_element(By.XPATH, "//*[@id='main']/app-select-date/div/div[4]/app-progress-button/button")
        continueBtn2.click()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        