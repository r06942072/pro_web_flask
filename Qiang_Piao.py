import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from fun import se

class buy_ticket():
    def __init__(self, departure, depart_id, destination, dest_id, date, quantity, email, password):
	
        
        driver.get("https://www.amtrak.com/home")
        self.departure = departure
        self.depart_id = depart_id
        self.destination = destination
        self.dest_id = dest_id
        #MM/DD/YY
        self.date = date
        self.quantity = quantity
        self.email = email
        self.password = password
    def input_information(self):

        se.send_keys_by_xpath(driver, '//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[2]/div/div[1]/div/div/div/input[2]', self.departure)
        #time.sleep(1)
        se.click_by_id(driver, self.depart_id)

        se.send_keys_by_xpath(driver, '//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div/input[2]', self.destination)
        #time.sleep(1)
        se.click_by_id(driver, self.dest_id)

        se.send_keys_by_xpath(driver, '//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div/div[2]/input', self.date)
        
        se.click_by_xpath(driver, '//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[4]/div[1]/div[2]')
        #pos = driver.find_element_by_xpath('//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[4]/div[2]/div[1]/ul/li[2]/div/div[2]/input')
        #pos.clear()
        #pos.send_keys(self.quantity)
        #se.send_keys_by_name(driver, '/sessionWorkflow/productWorkflow[@product='Rail']/tripRequirements/allJourneyRequirements/@adultTravellers', self.quantity)
        se.click_by_id(driver, 'findtrains')

    def pick_train(self):
        se.click_by_name(driver, "/sessionWorkflow/productWorkflow[@product='Rail']/selectedJourney[1]/@selectedPassengerFareBeanKey")
        se.click_by_xpath(driver, "/html/body/div[3]/div/div/div[3]/div[2]/div[3]/form[1]/table/tbody/tr[3]/td/div/input")
        se.click_by_xpath(driver, "/html/body/div[2]/div/div/div[2]/form/div[2]/div[2]/input")
    def log_in(self):
        driver.find_element_by_id('email').send_keys(self.email)
        driver.find_element_by_id( 'password').send_keys(self.password)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div/div[3]/input").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/form/div[3]/div/div/div[1]/div/p[3]/label/span[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/form/div[4]/div[2]/input").click()            
    def main(self):
   
        self.input_information()
        self.pick_train()
        self.log_in()

if __name__=='__main__':
    
    begin = time.time()
    print(begin)
    print(type(begin))	
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    obj = buy_ticket('WAS', 'WAS', 'Boston, MA', 'BOS', '03/28/2019', '2','anong9420@gmail.com', 'Deming0519@')
    obj.main()
    end = time.time()
    T = int(end-begin)
    print("total_time = %d sec" %T)	
