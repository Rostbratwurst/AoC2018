from selenium import webdriver
from collections import Counter
import itertools
import math

def getPuzzleinput(day):

    driver = webdriver.Chrome()
    driver.get('https://adventofcode.com/2018/day/'+str(day))
    # url="https://adventofcode.com/"
    # webbrowser.open(url,new=2)

    elem1 = driver.find_element_by_link_text('[GitHub]')
    elem1.click()

    driver.find_element_by_id('login_field').send_keys('Rostbratwurst')
    driver.find_element_by_id('password').send_keys('Puller100')
    driver.find_element_by_name('commit').click()

    elem1 = driver.find_element_by_link_text('get your puzzle input')
    elem1.click()

    driver.switch_to.window(driver.window_handles[1])
    inp = driver.find_element_by_tag_name("body")
    dayInput=inp.text.split('\n')
    print(dayInput)
    driver.quit()
    return dayInput

def lettercount(list_of_strings):

    twotimes=int(0)
    threetimes=int(0)

    for string in list_of_strings:
        counter = Counter(string)
        counter_counter=Counter(counter.values())

        if counter_counter[2]>=1:
            twotimes+=1

        if counter_counter[3]>=1:
            threetimes+=1


    return twotimes,threetimes

def checksum(args):
    result=1
    for i in args:
        result=result*i
    return result

def similarity(list):

    for st1,st2 in itertools.combinations(list,2):
        diff=0
        for c1,c2 in zip(st1,st2):
            if c1 != c2:
                diff+=1
                diffletter=[c1,c2]
        if diff==1:
            print(st1)
            print(st2)
            print(diffletter)





if __name__=="__main__":

    var=getPuzzleinput(2)
    resultsum=checksum(lettercount(var))
    part2=similarity(var)
