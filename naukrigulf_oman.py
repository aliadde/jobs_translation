from seleniumbase import BaseCase 
from time import sleep 
import json


BaseCase.main(__name__, __file__)

class MyTestClass(BaseCase):
    def test_oman_links(self):
        self.open("https://www.naukrigulf.com/jobs-in-oman?locale=en")
        sleep(1)
        self.maximize_window()
        sleep(5)
        # list to store urls 

        
        # getting a Tag of all same 
        links = self.find_elements("div.ng-box.srp-tuple a:first-of-type")
        
        list_of_links = []
        # loop and print the elements 
        for link in links: 
            # getting hreft in link 
            l = link.get_attribute("href")
            
            # write in string
            x = f"{l}"
            # add that string to list
            list_of_links.append(x)
            # print the string link 
            print(x)
        
        print("\n\n")
        with open("oman_links.txt" , "w") as file:
            for link in list_of_links:
                
                print(link)

                # write link in file 
                file.write(f"{link}\n")        
                
    