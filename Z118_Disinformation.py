#THIS IS TO BE USED ON LOCAL MACHINES ONLY
#THIS IS NOT TO BE USED ON WEB FACING PHISHING CAMPAIGNS
#THIS TOOL IS NOT FOR MALICIOUS USE, IT IS A RESEARCH TOOL CREATED FOR A SPECIFIC PHISHING CAMPAIGN HOSTED LOCALLY 

import socket
import os
import urllib
import requests
import struct
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning


#Lists
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
first_name = ["John", "Steve", "Karen", "Tylor", "Bob", "Rose", "Silva", "Darrel", "Jerome", "Tyrone", "Donald", "Steven", "Leslie", "Ann", "Nicole", "Smith", "Perry", "Barrymore", "Drew", "Carrey", "Lamar", "Billie", "Hannah", "Michelle", "Elizabeth", "Henry", "Luis", "Luiz", "Luise"]
last_name = ["Smith", "Valero", "Martinez", "Cruz", "Shiv", "Freeman", "Chavez", "Gonzales", "Stein", "Vlad", "Shelduchink", "Perry", "Hanks", "Washington", "Tarintino", "Fisher", "Thompson"]
street_name = ["River Side", "64th", "63rd", "62nd", "61st", "47th", "Shining Star", "Franklin", "Shoal", "River", "Lake", "Ocean", "Francisco", "Sunrise", "Dale", "8 Mile", "13th"]
street_end = ["Way", "Ct", "Rd", "Wy", "Court", "Road", "Blvd", "Boulevard", "Pass", "Ps"]
cities = ["Alexandria", "Auroa", "Austin", "Boston", "Chandler", "Charlotte", "Dallas", "Dayton", "Elizabeth", "Eugene", "Gilbert", "Houston", "Jackson", "Lincoln", "Madison", "Memphis", "Orlando", "Phoenix", "Savannah", "Warren", "San Francisco", " San Jose", " Los Angeles", " New York"]
states = ["California", "Nevada", "Oregon", "Washington", "Utah", "Idaho", "Wyoming", "Colorado", "New Mexico", "Illinois", "New York", "Maine", "South Carolina", "North Carolina", "Florida", "Washington D.C", "Kentucky"]
pw_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$"]

def fake_name():
    #Random Names
    first_num = random.randint(0, 27)
    last_num = random.randint(0, 15)
    #FullName
    full_name = "{} {}"
    email = "{}{}"
    full_name = full_name.format(first_name[first_num], last_name[last_num])
    email = email.format(first_name[first_num], last_name[last_num])
    return full_name, email

def fake_email():
    #Email
    full_name, email = fake_name()
    email = email.replace(" ", "")
    return full_name, email

def fake_address():
    #Addresses Numbers
    rand_num = random.randint(0, 6)
    send = ""
    for i in range(0, 6):
        if i != rand_num:
            send += numbers[rand_num]
            rand_num = random.randint(0, 6)
    street_num = random.randint(0, 16)
    end_num = random.randint(0, 9)
    full_address = str((send, street_name[street_num], street_end[end_num]))
    full_address = full_address.replace("(", "")
    full_address = full_address.replace(")", "")
    full_address = full_address.replace(",", "")
    full_address = full_address.replace("'", "")
    #Cities/States
    city_num = random.randint(0, 23)
    state_num = random.randint(0, 15)
    city = cities[city_num]
    state = states[state_num]
    #Zip Codes
    zip = ""
    for i in range(5):
        zip += numbers[rand_num]
        rand_num = random.randint(0, 9)
    return full_address, city, state, zip


def fake_creditcard():
    full_name, email = fake_email()
    #Fake Card Info
    card_holder = full_name
    fake_ccn = ""
    rand_num = random.randint(0, 9)
    for i in range (16):
        fake_ccn += numbers[rand_num]
        rand_num = random.randint(0, 9)
    fake_ccn = fake_ccn[:4] + " " + fake_ccn[4:8] + " " + fake_ccn[8:12] + " " + fake_ccn[12:16]
    exp_month = ""
    exp_year = "2"
    for i in range (2):
        rand_num = random.randint(0, 2)
        exp_month += numbers[rand_num]
    if exp_year == "2":
        rand_num = random.randint(2,8)
        exp_year += numbers[rand_num]
    fake_cvc = ""
    for i in range (3):
        fake_cvc += numbers[rand_num]
        rand_num = random.randint(0 ,9)
    exp_date = exp_month + "/" + exp_year
    return fake_ccn, exp_date, fake_cvc, full_name, email

def fake_birthday():
    #Fake Birthday
    day = ""
    month = "0"
    year = "19"
    for i in range (2):
        rand_num = random.randint(0, 2)
        day = numbers[rand_num]
        rand_num = random.randint(0, 9)
        day += numbers[rand_num]
    if month == "0":
        rand_num = random.randint(1, 9)
        month +=numbers[rand_num]
    for i in range(2):
        rand_num = random.randint(5, 9)
        year += numbers[rand_num]
    return day, month, year
def fake_password():
    #Fake Password
    password = ""
    password_gen = random.randint(4, 20)
    for i in range (password_gen):
        rand_num = random.randint(0, 55)
        password += pw_chars[rand_num]
    return password

def fake_ssn():
    #Fake SSN
    ssn = ""
    for i in range (9):
        rand_num = random.randint(0, 9)
        ssn += numbers[rand_num]
    ssn0 = ssn[:3]
    ssn1 = ssn[3:5]
    ssn2 = ssn[5:9]
    return ssn0, ssn1, ssn2

def fake_phonenum():
    #Fake Phone Number
    phone_num = ""
    for i in range (10):
        rand_num = random.randint(0, 9)
        phone_num += numbers[rand_num]
    phone_num0 = phone_num
    phone_num1 = phone_num[:6] + "-" + phone_num[6:]
    phone_num2 = phone_num[:3] + "-" + phone_num[3:6] + "-" + phone_num[6:]
    phone_num3 = phone_num0[:0] + "(" + phone_num0[0:3] + ")" + phone_num0[3:]
    phone_num4 = phone_num0[:0] + "(" + phone_num0[0:3] + ")" + phone_num0[3:6] + "-" + phone_num0[6:]
    phone_num5 = phone_num0[:0]  + phone_num0[0:3] + "-" + phone_num0[3:6] + "-" + phone_num0[6:]
    phone_num = [phone_num0, phone_num1, phone_num2, phone_num3, phone_num4, phone_num5]
    phone_rand = random.randint(0, 5)
    phone_num = phone_num[phone_rand]
    return phone_num

login_headers = {
    'POST': '/home/signin/Security/myaccount/signin/?country.x=US&locale.x=en_US HTTP/1.1',
    'HOST': 'https://127.0.0.1:443',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '50',
    'Origin': 'https://127.0.0.1:443',
    'Connection': 'close',
    'Referer': 'https://127.0.0.1:443/home/signin/Security/myaccount/signin/?country.x=US&locale.x=en_US',
    'Cookie': 'PHPSESSID=9812f06c853c2b353e8d23eb8087422b',
    'Upgrade-Insecure-Requests': '1'
}


def gen_fakeinfo():
    phone_num = fake_phonenum()
    ssn0, ssn1, ssn2 = fake_ssn()
    password = fake_password()
    day, month, year = fake_birthday()
    fake_ccn, exp_date, fake_cvc, full_name, email = fake_creditcard()
    full_address, city, state, zip = fake_address()
    #Generate Email (Didnt work in its own function)
    end_num = ""
    rand_email = random.randint(0, 4)
    for i in range (rand_email):
        email_num = random.randint(0, 9)
        end_num += numbers[email_num]
    email0 = email + str(end_num)
    email1 = email
    email2 = email.lower()
    email = [email0, email1, email2]
    extensions = ["@yahoo.com", "@gmail.com", "@hotmail.com", "@apple.com", "@microsoft.com", "@facebook.com", "@protonmail.com"]
    email_sel = random.randint(0, 2)
    extension_sel = random.randint(0, 6)
    email = email[email_sel] + extensions[extension_sel]
    email = email.replace(" ", "")
    login_post = {
    'login_email': email,
    'login_password':password
    }
    cardscam_post = {
    'fullname': full_name,
    'address': full_address,
    'city': city,
    'state': state,
    'zipCode': zip,
    'nameoncard': full_name,
    'cardnumber': fake_ccn,
    'expdate': exp_date,
    'csc': fake_cvc
    }
    ssnscam_post = {
    'day': day,
    'month': month,
    'year': year,
    'password_vbv': password,
    'ssn1': ssn0,
    'ssn2': ssn1,
    'ssn3': ssn2,
    'phoneE': "1",
    'phoneE_numb': phone_num,
    'vbv_submit_btn': "Submit"
    }

    return login_post, cardscam_post, ssnscam_post


def main_function():
    #URLS
    login_page = "https://127.0.0.1:443/home/signin/Security/myaccount/signin/?country.x=US&locale.x=en_US"
    card_page = "https://127.0.0.1:443/home/signin/Security/myaccount/settings/?verify_account=session=US&{}&dispatch={}"
    ssn_page = "https://127.0.0.1:443/home/signin/Security/myaccount/security/?secure_code=session=US&{}&dispatch={}"
    #Generate New Info
    login_post, cardscam_post, ssnscam_post = gen_fakeinfo()
    print("[+] New Info Has Been Generated")
    #Send First Login Post & Grab URLToken
    s = requests.Session()
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    r = s.post(login_page, headers=login_headers, data=login_post, verify=False)
    urlToken = (r.url)
    #Format URLToken
    tokenLength = len("https://127.0.0.1:443/home/signin/Security/myaccount/settings/?verify_account=session=&")
    urlToken = urlToken[tokenLength:]
    urlToken = urlToken.replace("dispatch=", "")
    urlToken = urlToken.split("&")
    print("[+] First Session and Dispatch Found!:", urlToken, "")
    #Format URL
    card_page = card_page.format(urlToken[0], urlToken[1])
    card_header = {'Host': 'https://127.0.0.1:443', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': '174', 'Origin': 'https://127.0.0.1:443', 'Connection': 'close', 'Referer': card_page, 'Cookie': 'PHPSESSID=9812f06c853c2b353e8d23eb8087422b', 'Upgrade-Insecure-Requests': '1' }
    #Send Fake Card Info & Grab 2nd URLToken
    r = s.post(card_page, headers=card_header, data=cardscam_post, verify=False)
    #Format 2nd URLToken
    urlToken2 = (r.url)
    tokenLength2 = len("https://127.0.0.1:443/home/signin/Security/myaccount/security/?secure_code=session=US&")
    urlToken2 = urlToken2[tokenLength2:]
    urlToken2 = urlToken2.replace("dispatch=", "")
    urlToken2 = urlToken2.split("&")
    urlToken2.remove("")
    print("[+] Second Session and Dispatch Found!:", urlToken2, "")
    #ssn_page 
    ssn_page = ssn_page.format(urlToken2[0], urlToken2[1])
    ssn_header = {'Host': 'https://127.0.0.1:443', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': '174', 'Origin': 'https://127.0.0.1:443', 'Connection': 'close', 'Referer': ssn_page, 'Cookie': 'PHPSESSID=9812f06c853c2b353e8d23eb8087422b', 'Upgrade-Insecure-Requests': '1' }
    #Send Fake SSN Info
    r = s.post(ssn_page, headers=ssn_header, data=ssnscam_post, verify=False)
    print("[!] Now Looping!\n")
    main_function()

main_function()

