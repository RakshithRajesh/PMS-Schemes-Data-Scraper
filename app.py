from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.binary_location = "path to browser"
driver_path = "path to chromedriver"
driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get("https://pmsbazaar.com/Home/Login")

### LOGIN PART ###
USERNAME = ""
PASSWORD = ""

username = driver.find_element_by_id("UserName").send_keys(USERNAME)
password = driver.find_element_by_id("Password").send_keys(PASSWORD)
submit = driver.find_element_by_id("btnLogin").click()
time.sleep(20)
print("Logged in SuccessFully!!!")


### SCRAPING ###
# 1) SCHEME NAME ##
scheme_names = driver.find_elements_by_css_selector('h4[data-bind="text: SchemeName"]')
scheme_name_list = []

for scheme_name in scheme_names:
    scheme_name_list.append(scheme_name.text)


## 2) CATEGORY NAME ##
scheme_categories = driver.find_elements_by_css_selector('small[data-bind="text: Category"]')
scheme_category_list = []

for scheme_category in scheme_categories:
    scheme_category_list.append(scheme_category.text)


## 3) PORTFOLIO AGE ##
scheme_ages = driver.find_elements_by_css_selector('span[data-bind="text: PortfolioAge"]')
scheme_age_list = []

for scheme_age in scheme_ages:
    scheme_age_list.append(scheme_age.text)


# 4) INCEPTION DATE ##
inception_dates = driver.find_elements_by_css_selector('span[data-bind="text: InceptionDate"]')
inception_date_list = []

for inception_date in inception_dates:
    inception_date_list.append(inception_date.text)


# 5) AUM IN CRS ##
aum_in_crs = driver.find_elements_by_css_selector('span[data-bind="text: AUM"]')
aum_list = []

for aum_in_cr in aum_in_crs:
    aum_list.append(aum_in_cr.text)

## 6) RETURNS ##
returnsall = driver.find_elements_by_css_selector('tr[class="border-bottom text-nowrap"]')
one_month = []
three_month = []
six_month = []
one_year = []
two_year = []
three_year = []
five_year = []
sis = []


for returns in returnsall:
    return_list = returns.text.split(" ")

    one_month.append(return_list[0])
    three_month.append(return_list[1])
    six_month.append(return_list[2])
    one_year.append(return_list[3])
    two_year.append(return_list[4])
    three_year.append(return_list[5])
    five_year.append(return_list[6])
    sis.append(return_list[7])


## 3) RETURNS SCRAPING ##
next_page_btn = driver.find_element_by_link_text(">")

for i in range(11):
    if next_page_btn:

        try:
            driver.implicitly_wait(40)
            next_page_btn.click()

            ## 1) SCHEME NAME ##
            scheme_names = driver.find_elements_by_css_selector('h4[data-bind="text: SchemeName"]')

            print(len(scheme_names))

            for scheme_name in scheme_names:
                scheme_name_list.append(scheme_name.text)


            ## 2) CATEGORY ##
            scheme_categories = driver.find_elements_by_css_selector('small[data-bind="text: Category"]')

            print(len(scheme_categories))

            for scheme_category in scheme_categories:
                scheme_category_list.append(scheme_category.text)


            ## 3) PORTFOLIO AGE ##
            scheme_ages = driver.find_elements_by_css_selector('span[data-bind="text: PortfolioAge"]')

            print(len(scheme_ages))

            for scheme_age in scheme_ages:
                scheme_age_list.append(scheme_age.text)

            
            ## 4) INCEPTION DATE ##
            inception_dates = driver.find_elements_by_css_selector('span[data-bind="text: InceptionDate"]')

            print(len(inception_dates))

            for inception_date in inception_dates:
                inception_date_list.append(inception_date.text)


            ## 5) AUM IN CRS ##
            aum_in_crs = driver.find_elements_by_css_selector('span[data-bind="text: AUM"]')

            print(len(aum_in_crs))

            for aum_in_cr in aum_in_crs:
                aum_list.append(aum_in_cr.text)

            ## 6) RETURNS ##
            returnsall = driver.find_elements_by_css_selector(
                'tr[class="border-bottom text-nowrap"]'
            )

            print(len(returnsall))

            for returns in returnsall:
                return_list = returns.text.split(" ")

                one_month.append(return_list[0])
                three_month.append(return_list[1])
                six_month.append(return_list[2])
                one_year.append(return_list[3])
                two_year.append(return_list[4])
                three_year.append(return_list[5])
                five_year.append(return_list[6])
                sis.append(return_list[7])

        except:
            print("Could not Click")


print(len(scheme_name_list))
print(len(scheme_category_list))
print(len(scheme_age_list))
print(len(inception_date_list))
print(len(aum_list))
print(len(one_month))
print(len(three_month))
print(len(six_month))
print(len(one_year))
print(len(three_year))
print(len(five_year))
print(len(sis))

df = pd.DataFrame(
    {"Scheme Name": scheme_name_list, 
    "Scheme Category": scheme_category_list, 
    "Scheme Age": scheme_age_list, 
    "Inception Date": inception_date_list,
    "Aum in Crs": aum_list,
    "1M": one_month,
    "3M": three_month,
    "6M": six_month,
    "1Y": one_year,
    "2Y": two_year,
    "3Y": three_year,
    "5Y": five_year,
    "SI": sis,}
)
df.to_csv("NCPAR.xlsx")
