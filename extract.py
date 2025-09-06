from seleniumbase import BaseCase 
from time import sleep 
import json
import subprocess

# BaseCase.main(__name__, __file__)

class MyTestClass(BaseCase):
      def test_extract_data(self): 
            # open the file 
            with open("oman_links.txt", "r") as file:
                  # read file and store in variable
                  content  = file.readlines()
                  # store in list to be retailable 
                  content = [line.strip() for line in content]

            # jobs dictionary for dumping to json 
            all_jobs = []

            # count the links with bash
            number_links = subprocess.run("cat oman_links.txt | wc -l",shell=True, )

            
            for i in range(0,2):
                  # get first link 
                  link = content[i]
                  # open first link
                  print(f"link_{i}:  ",link)
                  self.open(link)
                  sleep(10)

                  # export data with selector and getting text
                  print(" __________HEADER________ ")
                  title = self.find_element(".jd-info h1").text
                  print("title: ", title)

                  if self.is_text_visible(text="Employer Active"):
                        employer_active = self.find_element(".label-gold").text
                        print("time valiable:", employer_active)


                  time_stamp =  self.find_element(".time-stamp").text
                  print("time stamp: ", time_stamp)
                  
                  print("_____BODY____")
                  
                  experience = self.find_element("div.row:nth-child(1) > div:nth-child(1) > p:nth-child(2)").text
                  print("experience: ", experience)

                  if self.is_text_visible(text="Monthly Salary"):
                        monthly_salary = self.find_element("div.row:nth-child(1) > div:nth-child(2) > p:nth-child(2) > span:nth-child(1)").text
                        print("monthly_salary: ", monthly_salary)
                  

                  job_location = self.find_element("div.row:nth-child(1) > div:nth-child(3) > p:nth-child(2)").text
                  print("job location: ", job_location)

                  education = self.find_element("div.row:nth-child(2) > div:nth-child(1) > p:nth-child(2)").text
                  print("education: ", education)

                  nationality = self.find_element("div.row:nth-child(2) > div:nth-child(2) > p:nth-child(2)").text
                  print("nationality: ", nationality)            
                  
                  gender  = self.find_element("div.row:nth-child(2) > div:nth-child(3) > p:nth-child(2)").text
                  print("Gender: ", gender )

                  vacancy  = self.find_element("div.row:nth-child(2) > div:nth-child(3) > p:nth-child(2)").text
                  print("vacancy: ", vacancy )

                  # Job Description section 
                  
                  print("__________Job Description__________")
                  # get the Job Deskcription word
                  # job_description  = self.find_element(".heading.jdMain").text
                  # print("Job Description: ", job_description )
                  
                  # roles_and_responsibilities
                  elements = self.find_elements("/html/body/div[1]/div[2]/main/div[1]/section[1]/div[3]/article[1]/section/div/ul/li")
                  
                  # xtract text then put in a list then with .join export list to string with \n space between elements
                  roles_and_responsibilities = "\n".join([el.text for el in elements]) 
                  print("roles_and_responsibilities:", roles_and_responsibilities)

                  # key responsibilites
                  if self.is_text_visible("key responsibilites"):
                        key_elements = self.find_elements("div.paragraph > ul:nth-child(3) > li")
                        key_responsibilities = "\n".join([el.text for el in key_elements])
                        print("key_responsibilities:", key_responsibilities)
                  else:
                        print("key_responsibilities:", "")

                  # Desired Candidate Profile
                  if self.is_text_visible(text="Desired Candidate Profile"):
                        ele = self.find_elements("article.job-description:nth-child(3) > section:nth-child(1) > p:nth-child(2) > ul:nth-child(2) > li")
                        desired_candidate_profile = "\n".join([el.text for el in ele])      
                        print("desired_candidate_profile:", desired_candidate_profile)
                        
                  # Employment Type
                  if self.is_text_visible(text="Employment Type"):
                        employment_type  = self.find_element("div.job-description:nth-child(4) > ul:nth-child(2)").text
                        print("employment_type: ", employment_type)
                  
                  # Company Industry
                  if self.is_text_visible(text="Company Industry") :
                        coi = self.find_elements("div.job-description:nth-child(5) > ul:nth-child(2) > li")
                        company_industry = "/".join([el.text for el in coi])
                        print("company_industry : ", company_industry)
                  
                  # Department / Functional Area
                  if self.is_text_visible(text="Department / Functional Area"): 
                        dfa = self.find_elements("div.job-description:nth-child(6) > ul:nth-child(2) > li")
                        department_functional_area = "/".join([el.text for el in dfa])
                        print("Department / Functional Area :", department_functional_area)
                  
                  
                  

                  # create dictionary 
                  job_data = {
                        "title": title,
                        "employer_active": employer_active if self.is_text_visible(text="Employer Active") else "",
                        "time_stamp": time_stamp,
                        "experience": experience,
                        "monthly_salary": monthly_salary if self.is_text_visible(text="Monthly Salary") else "",
                        "job_location": job_location,
                        "education": education,
                        "nationality": nationality,
                        "gender": gender,
                        "vacancy": vacancy,
                        "roles_and_responsibilities": roles_and_responsibilities ,
                        "key_responsibilities": key_responsibilities if  self.is_text_visible(text="key responsibilites") else "",
                        "desired_candidate_profile": desired_candidate_profile if self.is_text_visible(text="Desired Candidate Profile") else "",
                        "employment_type": employment_type if self.is_text_visible(text="Employment Type") else "",
                        "company_industry": company_industry if self.is_text_visible(text="Company Industry") else "",
                        "department_functional_area": department_functional_area if self.is_text_visible(text="Department / Functional Area") else ""
                  }
                  
                  all_jobs.append(job_data)
                  # dump that dict to a new json file with same name as title of job

            with open("jobs_data.json", "w", encoding="utf-8") as f:
                  json.dump(all_jobs, f, ensure_ascii=False, indent=4)
                  