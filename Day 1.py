from selenium import webdriver
import itertools

driver = webdriver.Chrome()

driver.get('https://adventofcode.com/2018/day/1')
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
el = driver.find_element_by_tag_name("body")
print(el.text)

inputday1 = el.text

driver.quit()

inputday1 = inputday1.split('\n')
# delinput=[r'\n','+','-']
inputday1 = [float(i) for i in inputday1]

result_part_one = sum(inputday1)

frequency_memory = []
frequency_value = 0
index=0

run=True
while run==True:

    for i in inputday1:
        index+=1
        frequency_value += i
        if frequency_value in frequency_memory:
            print('double frequency', frequency_value, 'at position', index)
            run=False
            break
        else:
            frequency_memory.append(frequency_value)
