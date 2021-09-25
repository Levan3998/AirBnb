

options1 = options.Options()
options1.add_argument("user-data-dir=C:/Users/Levan/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=options1)
driver.get('https://www.airbnb.com/?locale=en&_set_bev_on_new_domain=1632576550_NzVhZWFhN2VlODZm')
#open tab
city = 'Dahab'
check_in = ('3', ('November','11'), '2021')
check_out = ('10', ('November','11'), '2021')
crew = 2
len_opp = 10
email = 'yosefbot369@gmail.com'
password = 'Yosef!!!@'
album = 'Dahab, Égypte'#Lima, Perú'#'Tokyo, Japan'#'Amsterdam, Netherlands'
price_factor = 1
rate_factor = 1
time.sleep(2)
search_button = driver.find_element_by_xpath('//*[@id="bigsearch-query-detached-query-input"]')# input city
search_button.send_keys(city)
time.sleep(1)
driver.find_element_by_class_name('_g4jdzz').click()
time.sleep(0.4)
# input check in
flag = True
flag1 = True
check_m = check_in[1][0] + " " + check_in[2]
same_ = driver.find_elements_by_class_name('_116xafi')[-3] # check for same month as check in first
if (same_.text == check_m):
    flag = False
    flag1 = False
    m_ = driver.find_elements_by_class_name('_1lds9wb')[-2]
    n_ = m_.find_element_by_class_name('_cvkwaj')
    o_ = n_.find_elements_by_class_name('_k5mfsv')
while(flag):
    m_ = driver.find_elements_by_class_name('_116xafi')[-1]
    if(m_.text == check_m):
        flag = False
    else:
        move_button = driver.find_elements_by_class_name('_187sg6v')[-1]
        move_button.click()
if(flag1):
    m_ = driver.find_elements_by_class_name('_1lds9wb')[-1]
    n_ = m_.find_element_by_class_name('_cvkwaj')
    o_ = n_.find_elements_by_class_name('_k5mfsv')
for i in o_:
    if(i.text == check_in[0]):
        i.click()


# input check out
check_m = check_out[1][0] + " " + check_out[2]
flag = True
same_ = driver.find_elements_by_class_name('_116xafi')[-2] # check for same month as check in first
if (same_.text == check_m):
    flag = False
while(flag):
    m_ = driver.find_elements_by_class_name('_116xafi')[-1]
    if(m_.text == check_m):
        flag = False
    else:
        move_button = driver.find_elements_by_class_name('_187sg6v')[-1]
        move_button.click()

m_ = driver.find_elements_by_class_name('_1lds9wb')[-1]
n_ = m_.find_element_by_class_name('_cvkwaj')
o_ = n_.find_elements_by_class_name('_k5mfsv')
for i in o_:
    if(i.text == check_out[0]):
        i.click()

guests = driver.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div[1]/div')# guests
guests.click()
for i in range(crew):
    driver.find_element_by_xpath('//*[@id="stepper-adults"]/button[2]/span').click()


driver.find_element_by_class_name('_1mzhry13').click()# search for resaults

############################################################################################


########################################################################################################
time.sleep(3)
try:
    driver.find_element_by_xpath('//*[@id="ExploreLayoutController"]/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/a').click()
    time.sleep(3)
except:
    print("Puta!")
########################################################################################################
def clean_price(txt):
    x1 = txt.split(" ")[0][1:]
    new_x = ""
    for n in x1:
        if(n != ','):
            new_x += n
    return new_x
L = []
x = int(driver.find_elements_by_class_name('_1y623pm')[-1].text)
for j in range(x):
    stays = driver.find_elements_by_class_name('_8ssblpx')
    for i in stays[1:-1]:
        link = i.find_element_by_class_name('_mm360j').get_attribute('href')
        x_ = clean_price(i.find_element_by_class_name('_krjbj').text)
        if (x_.isnumeric()):
            x_ = int(x_)
        else:
            x_ = 100000000
        try:
            y = float(i.find_element_by_class_name('_10fy1f8').text)
            z = float(i.find_element_by_class_name('_a7a5sx').text.split(' ')[1][1:])
        except:
            y = 1
            z = 1
        sum = (((10*y*z)**rate_factor)/x_**price_factor)
        L.append((sum,link))
    driver.find_element_by_class_name('_za9j7e').click()
    time.sleep(2)

L = sorted(L,key = lambda  tup : tup[0])
L = L[::-1][:len_opp]
R = []
for i in L:
    R.append((float(i[0]),str(i[1])))
R.sort(key = lambda tup : float(tup[0]))
R = R[::-1][:5]
temp_str = ""
with open('best offers.txt', 'w') as f:
    for j in R:
        temp_str += j[1] + '\n'
    f.write(temp_str)
##############################################Likes

L = []
with open ("best offers.txt",'r') as f:
    data = f.readlines()
    print(data)
    for line in data:
        line = line[0:-1]
        L.append(line)
for link in L:
    driver.get(link)
    time.sleep(2)
    state = True
    if (driver.find_element_by_class_name('_88xxct').find_elements_by_class_name('_5kaapu')[1].text == 'Save'):
        driver.find_elements_by_class_name('_mapkd4u')[1].click()
    else:
        state = False
    time.sleep(0.5)
    if(state):
        temp_elem = driver.find_elements_by_class_name('_ytmuji')
        j = None
        for i in temp_elem:
            if(i.text == album):
                j = i
        if not (j is None):
            j.click()
    time.sleep(2)
driver.close()
