
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import time



outfile = open('logfile.txt','w')



# Function 1 - Go to Login Page and log in

driver = webdriver.Firefox()
driver.get("http://www.contractsforgeeks.com/default.aspx")
time.sleep(2)
try:
	for a in range (9,91):
		a = a+1
		driver.find_element(By.XPATH, '//a[@href="javascript:selectPage('+str(a)+')"]').click()

		
		try:
			all_email = driver.find_elements(By.XPATH, '//div[@class="contactEmail"]/a')
			for email in all_email:
				email = email.text
				#print email
				outfile.write(email+'\n')
				
			
		except:
			print 'Error encountered'
			pass
		time.sleep(3)
except:
	pass
print "All done! Closing log file"
outfile.close()
driver.close()
