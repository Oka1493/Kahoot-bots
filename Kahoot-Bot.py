import chromedriver_binary
from sys import argv, exit
from selenium import webdriver
from time import sleep

if len(argv) != 4:
    exit("USAGE: python Kahoot-Bot.py [Game Pin] [Username] [Number Of Bots]")

def KahootBot(gamePIN,username,number_of_bots):
    driver = webdriver.Chrome()
    try: 
        for i in range(number_of_bots):    
            driver.get('https://kahoot.it/v2/')
            driver.find_element_by_name('gameId').send_keys(gamePIN)
            driver.find_element_by_tag_name('button').click()
            sleep(1)
            driver.find_element_by_name('nickname').send_keys(f'{username}{i+1}')
            driver.find_element_by_tag_name('button').click()
            if i != number_of_bots-1:
                driver.execute_script('window.open()')
                driver.switch_to.window(driver.window_handles[i+1])
            else:
                break
    except:
        print('Error has occurred: You may have entered the wrong game pin')

if __name__ == ¨__main__¨:
    KahootBot(argv[1],argv[2],argv[3])
    
