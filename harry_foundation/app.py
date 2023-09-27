#import Library
import os
import json
import time
from datetime import datetime 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random

#Load information
with open('./data/email.json', encoding='utf8') as load_email:
    EMAIL = json.load(load_email)

eml = EMAIL['test_email']['email']
psw = EMAIL['test_email']['pass']

path = os.getcwd()

opt = Options()
opt.add_argument("start-maximized")
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.notifications": 1 
})

###Process
#start session
now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
print('[harry_foundation][{0}] starting session'.format(now))
driver = webdriver.Chrome()
now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
print('[harry_foundation][{0}] search for "https://forms.gle/XwHH1GsVz38CB9mc9"'.format(now))
driver.get("https://forms.gle/XwHH1GsVz38CB9mc9")
time.sleep(.7)

for i in range(30):
    #Question1
    q1 = driver.find_element('xpath', '//*[@id="i8"]/div[3]/div')
    q1.click()
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 1 || 2002-2007'.format(now))

    #Question2
    q2_ran = random.randint(1, 2)
    if q2_ran == 1 :
        q2 = driver.find_element('xpath', '//*[@id="i18"]/div[3]/div')
        q2.click()
        ans = 'Male'
    elif q2_ran == 2:
        q2 = driver.find_element('xpath', '//*[@id="i21"]/div[3]/div')
        q2.click()
        ans = 'Female'
    else : pass
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 2 || {1}'.format(now, ans))

    #Next to page 2
    n1 = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    n1.click()
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] go to page 2'.format(now))
    time.sleep(.2)

    #Question3
    q3_ran = random.randint(1, 100)
    if q3_ran < 60 :
        q3 = driver.find_element('xpath', '//*[@id="i5"]/div[3]/div')
        q3.click()
        ans = 'Yes'
    else :
        q3 = driver.find_element('xpath', '//*[@id="i8"]/div[3]/div')
        q3.click()
        ans = 'No'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 3 || {1}'.format(now, ans))

    #Question4
    q4_ran = random.randint(1, 100)
    if q4_ran < 10 :
        q4 = driver.find_element('xpath', '//*[@id="i15"]/div[3]/div')
        q4.click()
        ans = 'No'
    elif q4_ran < 40 :
        q4 = driver.find_element('xpath', '//*[@id="i18"]/div[3]/div')
        q4.click()
        ans = 'Sometimes'
    else :
        q4 = driver.find_element('xpath', '//*[@id="i21"]/div[3]/div')
        q4.click()
        ans = 'Yes'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 4 || {1}'.format(now, ans))

    #Question5
    q5_ran = random.randint(1, 100)
    if q5_ran < 6 :
        q5 = driver.find_element('xpath', '//*[@id="i40"]/div[3]/div')
        q5.click()
        ans = '16-24 hour'
    elif q5_ran < 12 :
        q5 = driver.find_element('xpath', '//*[@id="i43"]/div[3]/div')
        q5.click()
        ans = 'More than 24 hour'
    elif q5_ran < 26 :
        q5 = driver.find_element('xpath', '//*[@id="i28"]/div[3]/div')
        q5.click()
        ans = ' Less than 2 hour'
    elif q5_ran < 50 :
        q5 = driver.find_element('xpath', '//*[@id="i31"]/div[3]/div')
        q5.click()
        ans = '2-6 hour'
    elif q5_ran < 70 :
        q5 = driver.find_element('xpath', '//*[@id="i37"]/div[3]/div')
        q5.click()
        ans = '10-16 hour'
    else :
        q5 = driver.find_element('xpath', '//*[@id="i34"]/div[3]/div')
        q5.click()
        ans = '4-10 hour'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 5 || {1}'.format(now, ans))

    #Question6
    q6_ran = random.randint(1, 100)
    if q6_ran < 10 :
        q6 = driver.find_element('xpath', '//*[@id="i54"]/div[2]')
        q6.click()
        ans = 'Console'
    elif q6_ran < 40 :
        q6 = driver.find_element('xpath', '//*[@id="i51"]/div[2]')
        q6.click()
        ans = 'PC'
    else :
        q6 = driver.find_element('xpath', '//*[@id="i57"]/div[2]')
        q6.click()
        ans = 'Mobile'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 6 || {1}'.format(now, ans))

    #Question7
    q7_ran = random.randint(1, 100)
    if q7_ran < 10 :
        q7 = driver.find_element('xpath', '//*[@id="i64"]/div[3]/div')
        q7.click()
        ans = 'Multiplayer'
    elif q7_ran < 25 :
        q7 = driver.find_element('xpath', '//*[@id="i67"]/div[3]/div')
        q7.click()
        ans = 'Singleplayer'
    else :
        q7 = driver.find_element('xpath', '//*[@id="i70"]/div[3]/div')
        q7.click()
        ans = 'Both'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 7 || {1}'.format(now, ans))

    #Question8
    q8_ran = random.randint(1, 5)
    if q8_ran == 1 :
        q8 = driver.find_element('xpath', '//*[@id="i78"]/div[2]')
        q8.click()
        ans = 'Rockstar'
    elif q8_ran == 2 :
        q8 = driver.find_element('xpath', '//*[@id="i81"]/div[2]')
        q8.click()
        ans = 'Sony'
    elif q8_ran == 3 :
        q8 = driver.find_element('xpath', '//*[@id="i84"]/div[2]')
        q8.click()
        ans = 'Ubisoft'
    elif q8_ran == 4 :
        q8 = driver.find_element('xpath', '//*[@id="i87"]/div[2]')
        q8.click()
        ans = 'EA'
    else :
        q8 = driver.find_element('xpath', '//*[@id="i90"]/div[2]')
        q8.click()
        ans = 'Blizzard Activision'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 8 || {1}'.format(now, ans))

    #Question9
    q9_ran = random.randint(1, 4)
    if q9_ran == 1 :
        q9 = driver.find_element('xpath', '//*[@id="i101"]/div[2]')
        q9.click()
        ans = 'Sci-fi'
    elif q9_ran == 2 :
        q9 = driver.find_element('xpath', '//*[@id="i104"]/div[2]')
        q9.click()
        ans = 'Retro'
    elif q9_ran == 3 :
        q9 = driver.find_element('xpath', '//*[@id="i107"]/div[2]')
        q9.click()
        ans = 'Anime'
    else :
        q9 = driver.find_element('xpath', '//*[@id="i110"]/div[2]')
        q9.click()
        ans = 'History'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 9 || {1}'.format(now, ans))

    #Question9
    q10_ran = random.randint(1, 8)
    if q10_ran == 1 :
        q10 = driver.find_element('xpath', '//*[@id="i121"]/div[2]')
        q10.click()
        ans = ' RPG'
    elif q10_ran == 2 :
        q10 = driver.find_element('xpath', '//*[@id="i124"]/div[2]')
        q10.click()
        ans = 'Action'
    elif q10_ran == 3 :
        q10 = driver.find_element('xpath', '//*[@id="i127"]/div[2]')
        q10.click()
        ans = 'Honnor'
    elif q10_ran == 4 :
        q10 = driver.find_element('xpath', '//*[@id="i130"]/div[2]')
        q10.click()
        ans = 'Stategy'
    elif q10_ran == 5 :
        q10 = driver.find_element('xpath', '//*[@id="i133"]/div[2]')
        q10.click()
        ans = 'Moba'
    elif q10_ran == 6 :
        q10 = driver.find_element('xpath', '//*[@id="i136"]/div[2]')
        q10.click()
        ans = 'Shooter'
    elif q10_ran == 7 :
        q10 = driver.find_element('xpath', '//*[@id="i139"]/div[2]')
        q10.click()
        ans = 'Simulation'
    else :
        q10 = driver.find_element('xpath', '//*[@id="i142"]/div[2]')
        q10.click()
        ans = 'Sport & Racing'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 10 || {1}'.format(now, ans))

    #Question7
    q11_ran = random.randint(1, 100)
    if q11_ran < 50 :
        if q11_ran < 20 :
            q11 = driver.find_element('xpath', '//*[@id="i150"]/div[2]')
            q11.click()
            ans = 'Free'
        elif q11_ran < 40 :
            q11 = driver.find_element('xpath', '//*[@id="i153"]/div[2]')
            q11.click()
            ans = '0-500 baht' 
        else :
            q11_1 = driver.find_element('xpath', '//*[@id="i150"]/div[2]')
            q11_2 = driver.find_element('xpath', '//*[@id="i153"]/div[2]')
            q11_1.click()
            q11_2.click()
            ans = 'Free and 0-500 baht'
    elif q11_ran < 70 :
        q11 = driver.find_element('xpath', '//*[@id="i156"]/div[2]')
        q11.click()
        ans = '501-1000 baht'
    elif q11_ran < 90 :
        q11 = driver.find_element('xpath', '//*[@id="i159"]/div[2]')
        q11.click()
        ans = '1001-1500 baht'
    elif q11_ran < 95 :
        q11 = driver.find_element('xpath', '//*[@id="i162"]/div[2]')
        q11.click()
        ans = '1501-2000 baht'
    else :
        q11 = driver.find_element('xpath', '//*[@id="i165"]/div[2]')
        q11.click()
        ans = 'more than 2000 baht'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 11 || {1}'.format(now, ans))

    #Question12
    q12_ran = random.randint(1, 100)
    if q12_ran < 40 :
        q12 = driver.find_element('xpath', '//*[@id="i173"]/div[2]')
        q12.click()
        ans = 'Steam'
    elif q12_ran < 55 :
        q12 = driver.find_element('xpath', '//*[@id="i179"]/div[2]')
        q12.click()
        ans = 'Epic games'
    elif q12_ran < 70 :
        q12 = driver.find_element('xpath', '//*[@id="i185"]/div[2]')
        q12.click()
        ans = 'Xbox'
    elif q12_ran < 80 :
        q12 = driver.find_element('xpath', '//*[@id="i188"]/div[2]')
        q12.click()
        ans = 'Playstation'
    elif q12_ran < 90 :
        q12 = driver.find_element('xpath', '//*[@id="i191"]/div[2]')
        q12.click()
        ans = 'Ubisoft connect'
    elif q12_ran < 95 :
        q12 = driver.find_element('xpath', '//*[@id="i173"]/div[2]')
        q12.click()
        ans = 'Physical disc'
    else :
        q12 = driver.find_element('xpath', '//*[@id="i182"]/div[2]')
        q12.click()
        ans = 'GOG'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 12 || {1}'.format(now, ans))

    #Question13
    q13_ran = random.randint(1, 100)
    if q13_ran < 30 :
        q13 = driver.find_element('xpath', '//*[@id="i201"]/div[3]/div')
        q13.click()
        ans = 'Yes'
    elif q13_ran < 50 :
        q13 = driver.find_element('xpath', '//*[@id="i204"]/div[3]/div')
        q13.click()
        ans = 'No'
    else :
        q13 = driver.find_element('xpath', '//*[@id="i207"]/div[3]/div')
        q13.click()
        ans = 'Sometimes'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 13 || {1}'.format(now, ans))

    #Question14
    q14_ran = random.randint(1, 100)
    if q14_ran < 30 :
        q14 = driver.find_element('xpath', '//*[@id="i215"]/div[2]')
        q14.click()
        ans = 'Social media'
    elif q14_ran < 60 :
        q14 = driver.find_element('xpath', '//*[@id="i221"]/div[2]')
        q14.click()
        ans = 'Friends'
    elif q14_ran < 85 :
        q14 = driver.find_element('xpath', '//*[@id="i224"]/div[2]')
        q14.click()
        ans = 'Advertisement'
    else :
        q14 = driver.find_element('xpath', '//*[@id="i218"]/div[2]')
        q14.click()
        ans = 'News'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 14 || {1}'.format(now, ans))

    #Question15
    q15_ran = random.randint(1, 100)
    if q15_ran < 50 :
        q15 = driver.find_element('xpath', '//*[@id="i234"]/div[3]/div')
        q15.click()
        ans = 'Yes'
    elif q15_ran < 45 :
        q15 = driver.find_element('xpath', '//*[@id="i240"]/div[3]/div')
        q15.click()
        ans = 'Sometimes'
    else :
        q15 = driver.find_element('xpath', '//*[@id="i237"]/div[3]/div')
        q15.click()
        ans = 'No'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 15 || {1}'.format(now, ans))

    #Next to page 3
    n2 = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')
    n2.click()
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] go to page 3'.format(now))
    time.sleep(.2)

    #Question16
    q16_ran = random.randint(1, 100)
    if q16_ran < 50 :
        q16 = driver.find_element('xpath', '//*[@id="i5"]/div[3]/div')
        q16.click()
        ans = 'Yes'
    elif q16_ran < 45 :
        q16 = driver.find_element('xpath', '//*[@id="i11"]/div[3]/div')
        q16.click()
        ans = 'Maybe'
    else :
        q16 = driver.find_element('xpath', '//*[@id="i8"]/div[3]/div')
        q16.click()
        ans = 'No'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 16 || {1}'.format(now, ans))

    #Question17
    q17_ran = random.randint(1, 100)
    if q17_ran < 25 :
        q17 = driver.find_element('xpath', '//*[@id="i18"]/div[3]')
        q17.click()
        ans = 'Yes'
    elif q17_ran < 50 :
        q17 = driver.find_element('xpath', '//*[@id="i21"]/div[3]')
        q17.click()
        ans = 'No'
    else :
        q17 = driver.find_element('xpath', '//*[@id="i24"]/div[3]')
        q17.click()
        ans = 'Sometimes'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 17 || {1}'.format(now, ans))

    #Question18
    q18_ran = random.randint(1, 100)
    if q18_ran < 30 :
        q18 = driver.find_element('xpath', '//*[@id="i32"]/div[2]')
        q18.click()
        ans = 'Social media'
    elif q18_ran < 60 :
        q18 = driver.find_element('xpath', '//*[@id="i38"]/div[2]')
        q18.click()
        ans = 'Friends'
    elif q18_ran < 85 :
        q18 = driver.find_element('xpath', '//*[@id="i41"]/div[2]')
        q18.click()
        ans = 'Advertisement'
    else :
        q18 = driver.find_element('xpath', '//*[@id="i35"]/div[2]')
        q18.click()
        ans = 'News'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 18 || {1}'.format(now, ans))

    #Question19
    q19_ran = random.randint(1, 100)
    if q19_ran < 50 :
        q19 = driver.find_element('xpath', '//*[@id="i51"]/div[3]/div')
        q19.click()
        ans = 'Yes'
    elif q19_ran < 60 :
        q19 = driver.find_element('xpath', '//*[@id="i54"]/div[3]/div')
        q19.click()
        ans = 'No'
    else :
        q19 = driver.find_element('xpath', '//*[@id="i57"]/div[3]/div')
        q19.click()
        ans = 'Sometimes'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 19 || {1}'.format(now, ans))

    #Question20
    q20_ran = random.randint(1, 100)
    if q20_ran < 50 :
        q20 = driver.find_element('xpath', '//*[@id="i64"]/div[3]/div')
        q20.click()
        ans = 'Yes'
    else :
        q20 = driver.find_element('xpath', '//*[@id="i67"]/div[3]/div')
        q20.click()
        ans = 'No'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 20 || {1}'.format(now, ans))

    #Question21
    q21_ran = random.randint(1, 100)
    if q21_ran < 50 :
        q21 = driver.find_element('xpath', '//*[@id="i74"]/div[3]/div')
        q21.click()
        ans = 'Yes'
    elif q21_ran < 60 :
        q21 = driver.find_element('xpath', '//*[@id="i77"]/div[3]/div')
        q21.click()
        ans = 'No'
    else :
        q21 = driver.find_element('xpath', '//*[@id="i80"]/div[3]/div')
        q21.click()
        ans = 'Sometimes'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 21 || {1}'.format(now, ans))

    #Question22
    q22_ran = random.randint(1, 100)
    if q22_ran < 60 :
        q22 = driver.find_element('xpath', '//*[@id="i87"]/div[3]/div')
        q22.click()
        ans = 'Yes'
    elif q22_ran < 85 :
        q22 = driver.find_element('xpath', '//*[@id="i90"]/div[3]/div')
        q22.click()
        ans = 'No'
    else :
        q22 = driver.find_element('xpath', '//*[@id="i93"]/div[3]/div')
        q22.click()
        ans = 'Sometimes'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 22 || {1}'.format(now, ans))

    #Question23
    q23_ran = random.randint(1, 100)
    if q23_ran < 50 :
        q23 = driver.find_element('xpath', '//*[@id="i100"]/div[3]/div')
        q23.click()
        ans = 'Yes'
    elif q23_ran < 65 :
        q23 = driver.find_element('xpath', '//*[@id="i103"]/div[3]/div')
        q23.click()
        ans = 'No'
    else :
        q23 = driver.find_element('xpath', '//*[@id="i106"]/div[3]/div')
        q23.click()
        ans = 'Sometimes'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 23 || {1}'.format(now, ans))

    #Question24
    q24_ran = random.randint(1, 100)
    if q24_ran < 25 :
        q24 = driver.find_element('xpath', '//*[@id="i114"]/div[2]')
        q24.click()
        ans = 'Yes'
    elif q24_ran < 50 :
        q24 = driver.find_element('xpath', '//*[@id="i117"]/div[2]')
        q24.click()
        ans = 'No'
    else :
        q24 = driver.find_element('xpath', '//*[@id="i120"]/div[2]')
        q24.click()
        ans = 'Sometimes'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 24 || {1}'.format(now, ans))

    #Question25
    q25_ran = random.randint(1, 100)
    if q25_ran < 30 :
        q25 = driver.find_element('xpath', '//*[@id="i127"]/div[3]/div')
        q25.click()
        ans = 'Yes'
    elif q25_ran < 30 :
        q25 = driver.find_element('xpath', '//*[@id="i130"]/div[3]/div')
        q25.click()
        ans = 'No'
    else :
        q25 = driver.find_element('xpath', '//*[@id="i133"]/div[3]/div')
        q25.click()
        ans = 'Sometimes'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 25 || {1}'.format(now, ans))

    #Question26
    q26_ran = random.randint(1, 100)
    if q26_ran < 25 :
        q26 = driver.find_element('xpath', '//*[@id="i140"]/div[3]/div')
        q26.click()
        ans = 'Yes'
    elif q26_ran < 50 :
        q26 = driver.find_element('xpath', '//*[@id="i143"]/div[3]/div')
        q26.click()
        ans = 'No'
    else :
        q26 = driver.find_element('xpath', '//*[@id="i146"]/div[3]/div')
        q26.click()
        ans = 'Sometimes'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 26 || {1}'.format(now, ans))

    #Question27
    q27_ran = random.randint(1, 100)
    if q27_ran < 65 :
        q27 = driver.find_element('xpath', '//*[@id="i153"]/div[3]/div')
        q27.click()
        ans = 'Yes'
    elif q27_ran < 80 :
        q27 = driver.find_element('xpath', '//*[@id="i156"]/div[3]/div')
        q27.click()
        ans = 'No'
    else :
        q27 = driver.find_element('xpath', '//*[@id="i159"]/div[3]/div')
        q27.click()
        ans = 'Sometimes'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 27 || {1}'.format(now, ans))

    #Question28
    q28_ran = random.randint(1, 100)
    if q28_ran < 30 :
        q28 = driver.find_element('xpath', '//*[@id="i166"]/div[3]/div')
        q28.click()
        ans = 'Yes'
    elif q28_ran < 60 :
        q28 = driver.find_element('xpath', '//*[@id="i169"]/div[3]/div')
        q28.click()
        ans = 'No'
    else :
        q28 = driver.find_element('xpath', '//*[@id="i172"]/div[3]/div')
        q28.click()
        ans = 'Sometimes'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 28 || {1}'.format(now, ans))

    #Question29
    q29_ran = random.randint(1, 100)
    if q29_ran < 25 :
        q29 = driver.find_element('xpath', '//*[@id="i180"]/div[2]') 
        q29.click()
        ans = 'Promotion'
    elif q29_ran < 50 :
        q29 =     driver.find_element('xpath', '//*[@id="i183"]/div[2]')
        q29.click()
        ans = 'Advertisement'
    elif q29_ran < 75 :
        q29 = driver.find_element('xpath', '//*[@id="i186"]/div[2]')
        q29.click()
        ans = 'friends'
    else :
        q29 = driver.find_element('xpath', '//*[@id="i189"]/div[2]')
        q29.click()
        ans = 'Price'
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] complete question 29 || {1}'.format(now, ans))

    #Submiting the form
    s = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    s.click()
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] Form submitted'.format(now))

    #/html/body/div[1]/div[2]/div[1]/div/div[4]/a 
    redo = driver.find_element('xpath', '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    redo.click()
    now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('[harry_foundation][{0}] redo the form'.format(now))
    print('[harry_foundation][{0}] loop : '.format(now),i+1)
    time.sleep(.3)

time.sleep(3)
driver.close()
now = "{0}:{1}:{2}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)
print('[harry_foundation][{0}] session closed'.format(now))