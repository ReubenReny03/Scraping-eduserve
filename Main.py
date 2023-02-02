from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import lxml
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path="link_to_the_chrome_driver",options=options)
driver.get("https://eduserve.karunya.edu/Login.aspx")
print("In eduserve...")
id_number=driver.find_element(By.ID,"mainContent_Login1_UserName")
id_number.send_keys("your_id")
passw =driver.find_element(By.ID,"mainContent_Login1_Password")
passw.send_keys("your_pass")
passw.send_keys(Keys.ENTER)
print("Waiting for authentication..")
driver.get("https://eduserve.karunya.edu/Student/TimeTable.aspx")
print("Authentication successfull..")
Semister =driver.find_element(By.ID,"mainContent_DDLACADEMICTERM")
Semister.click()
Semister.send_keys(Keys.DOWN)
Semister.send_keys(Keys.ENTER)
content = driver.page_source.encode("utf-8").strip()
edu_soup = BeautifulSoup(content,"lxml")
driver.get("https://eduserve.karunya.edu/Logout.aspx")
time.sleep(10)

with open("final_list.csv", 'a') as f:
        f.write("DAY,Hour 1,Hour 2,Hour 3,Hour 4,Hour 5,Hour 6,Hour 7,Hour 8,Hour 9")
        f.write("\n")

for x in range(5):
    final_soup = edu_soup.find("tr",{"id":f"ctl00_mainContent_grdData_ctl00__{x}"})
    my_list = []
    for x in final_soup:
        time_table = ""
        string_soup = x.text
        time_table = string_soup.replace("<td>","").replace("</td>","")
        if time_table == "\xa0":
            time_table = "FREE"
        my_list.append(time_table)
    with open("final_list.csv", 'a') as f:
        f.write(",".join(my_list[1:]))
        f.write("\n")
print("Full Report Generation Succesfull : )")
