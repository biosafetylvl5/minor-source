from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import argparse
import os

parser = argparse.ArgumentParser(description='Options for downloading scans')

parser.add_argument("-p", "--password", help="Login Password")
parser.add_argument("-e", "--email", help='Login Email')
parser.add_argument("-b", "--book", help='Book value') 
parser.add_argument("-l", "--limit", help='When to stop downloading pages')
parser.add_argument("-r", "--roman", help="Use roman charecters instead of normal numbers", action="store_true")
parser.add_argument("-a", "--path", help="Path to save files to")
parser.add_argument("-q", "--prefix", help="Prefix to add to pages (Example: A1, A2, ... )")
parser.add_argument("-w", "--wait", help="Time to wait in between pages. Default: 250")
parser.add_argument("-s", "--start", help="Page to start at. Default: 1")


parser.parse_args()
args = parser.parse_args()
if(args.limit):
    limit = args.limit
else:
    print "Limit not defined. Use -h to see help."
    exit()
if(args.book):
    book = args.book
else:
    print "Book number not defined. Use -h to see help."
    exit()
if(args.email):
    email = args.email 
else:
    print "Login email not defined. Use -h to see help."
    exit()
if(args.password):
    password = args.password
else:
    print "Login password not defined. Use -h to see help."
    exit()

if(args.wait):
    wait_time = args.wait
else:
    wait_time = 250

if(args.path):
    save_path = args.path
else:
    save_path = os.path.expanduser("~\Downloads\Book\\")
    
if(args.roman):
    roman = True
    try:
        import roman
    except:
        print "Error: module 'roman' not installed. \nInstall for roman charecter support from https://pypi.python.org/pypi/roman"
        exit()
else:
    roman = False
    
if(args.prefix):
    prefix=args.prefix
else:
    prefix=""

if(args.start):
    start=int(args.start)
else:
    start=0

print "Loading..."
profile = webdriver.FirefoxProfile()
profile.add_extension(extension='save_images-1.0.7-fx+sm.xpi')
profile.set_preference("extensions.SI.cbxSaveFolder", save_path)
profile.set_preference("extensions.SI.chkOpenDlg", False)
profile.set_preference("extensions.SI.shortcutkeys", "0,0,5,73,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,-27,3,79,0,0,0,0,3,90,")
profile.set_preference("javascript.enabled", False);
print "Opening Browser"
driver = webdriver.Firefox(profile)
print "Navigating to login page"
driver.get("http://online.vitalsource.com/signin") #Start the Signin Prosses
elem = driver.find_element_by_name("email")
elem.send_keys(email)
elem = driver.find_element_by_name("password")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
print "Logged in"
time.sleep(1)
x=start
while True:
    if int(x)>int(limit):
        print "Done!"
        driver.close()
        exit()
    if(roman):
        print "Downloading Page:"+str(roman.toRoman(x))
        print "Downloading Page:"+str(roman.toRoman(x+1))
        url = "http://online.vitalsource.com/books/"+book+"/print?from="+str(prefix)+str(roman.toRoman(x))+"&to="+str(prefix)+str(roman.toRoman((x+1)))+"&skip_desktop=false"
    else:
        print "Downloading Page:"+str(x)
        print "Downloading Page:"+str(x+1)
        url = "http://online.vitalsource.com/books/"+book+"/print?from="+str(prefix)+str(x)+"&to="+str(prefix)+str(x+1)+"&skip_desktop=false"
    driver.get(url)
    try: #check if signed out yet
        elem = driver.find_element_by_id("printhead")
        elem.send_keys(Keys.CONTROL, Keys.ALT, 'i')
        x=x+2
    except: #re-signin
        driver.get("http://online.vitalsource.com/signin")
        elem = driver.find_element_by_name("email")
        elem.send_keys(email)
        elem = driver.find_element_by_name("password")
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
        time.sleep(wait_time)

    