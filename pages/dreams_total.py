from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#dreams.total.html  --correct stats
class DreamsTotal:
    def __init__(self,driver):
        self.driver=driver
        self.my_dreams = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "dreamButton")))
        self.my_dreams.click()
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.number_of_windows_to_be(3))
        # test dreams-dairy and dreams-total active windows
        windows = self.driver.window_handles
        for window in windows:
            self.driver.switch_to.window(window)
            url = self.driver.current_url
            if "dreams-diary.html" in url:
                self.diary_window = window
            elif "dreams-total.html" in url:
                self.total_window = window

    def all_stats(self):
        self.driver.switch_to.window(self.total_window)
        dream_stats = self.driver.find_elements(By.XPATH, "//table[@id='dreamsTotal']//tbody//tr")
        expected_stats = {
            "Good Dreams": "6",
            "Bad Dreams": "4",
            "Total Dreams": "10",
            "Recurring Dreams": "2"
        }
        for row in dream_stats:
            column1 = row.find_element(By.XPATH, "./td[1]").text
            column2 = row.find_element(By.XPATH, "./td[2]").text
            if column1 in expected_stats.keys():
                assert column2 == expected_stats[column1], \
                    f"{column1} is not {expected_stats[column1]}"




