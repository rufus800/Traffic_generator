import selenium as se
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import random
import csv

def get_user_input():
    url = input("Enter destination URL: ")
    visits = int(input("Enter number of visits: "))
    return url, visits

def setup_driver(user_agent):
    options = Options()
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=options)
    return driver

def log_visit(user_agent, visit_number):
    with open('traffic3.log', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["User Agent", "Visit Number", "Timestamp"])
        writer.writerow([user_agent, visit_number, time.strftime('%Y-%m-%d %H:%M:%S')])

def main():
    url, visits = get_user_input()
    ua = UserAgent()

    for i in range(visits):
        user_agent = ua.random
        print(f"Visit {i + 1}: User Agent - {user_agent}")

        driver = None
        try:
            driver = setup_driver(user_agent)
            driver.get(url)
            driver.set_window_size(1120, 550)
            time.sleep(random.randint(2, 10))
            print(f"Current URL: {driver.current_url}")
            log_visit(user_agent, i + 1)
        except Exception as e:
            print(f"Error during visit {i + 1}: {e}")
        finally:
            if driver:
                driver.quit()

if __name__ == "__main__":
    main()
