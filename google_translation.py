import json
from seleniumbase import BaseCase

class GoogleTranslation(BaseCase):
    def test_translate_jobs(self,retries=3):
            # ---- 1. خواندن فایل جیسون ----
            with open("jobs_data.json", "r", encoding="utf-8") as f:
                  jobs = json.load(f)

            translated_jobs = []

            self.open("https://translate.google.com/?sl=en&tl=fa&op=translate")

            # cookie button pass
            self.wait_for_element_visible("#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.AIC7ge > div.CxJub > div.VtwTSb > form:nth-child(2) > div > div > button")
            self.click(selector="#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.AIC7ge > div.CxJub > div.VtwTSb > form:nth-child(2) > div > div > button")


            # ---- . برای هر آگهی ----
            for job in jobs:
                  tr_job = {} # new dictionary for that job  
                  for key, val in job.items():

                        # رشته‌ای که میخوای ترجمه کنی
                        text_to_translate = val

                        
                        if key == "job_description" or  key == "roles_and_responsibilities": # wait more 
                              # نوشتن متن
                              # write text="untranslated_eng_text" in the eng box to be translate
                              self.write(selector="#yDmH0d > c-wiz > div > div.ToWKne > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > div > c-wiz > span > span > div > textarea",
                                          text=text_to_translate)
                              self.sleep(4)
                        
                        else:
                              # نوشتن متن
                              # write text="untranslated_eng_text" in the eng box to be translate
                              self.write(selector="#yDmH0d > c-wiz > div > div.ToWKne > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > div > c-wiz > span > span > div > textarea",
                                          text=text_to_translate)
                              self.sleep(2.5)
                        
                        
                        # گرفتن خروجی
                        texts = self.find_elements("span.ryNqvb")
                        translated_text = "\n".join([el.text for el in texts])
                        
                        # اضافه کردن ترجمه به آگهی
                        tr_job[f"{key}_fa"] = translated_text

                  translated_jobs.append(tr_job)

                  # ---- 3. ذخیره خروجی ----
                  with open("all_jobs_translated.json", "w", encoding="utf-8") as f:
                        json.dump(translated_jobs, f, ensure_ascii=False, indent=4)

                  print("✅ ترجمه آگهی‌ها ذخیره شد در all_jobs_translated.json")
                  self.sleep(5)
