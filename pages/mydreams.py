from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoadingAnimation:
    def __init__(self,driver):
        self.driver=driver
        self.logo = self.driver.find_element(By.CLASS_NAME, "dream-icon")
        self.content = self.driver.find_element(By.ID, "mainContent")
        self.my_dreams = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "dreamButton")))
        self.wait = WebDriverWait(self.driver, 10)
    def loading_animation(self):
        WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.ID, "loadingAnimation")))

        # test logo
        assert self.logo.is_displayed(), "logo not displayed"

    def content_button(self):
        assert self.content.is_displayed(), "Main content is not displayed"
        assert self.my_dreams.is_displayed(), "My Dreams button is not displayed"

    def diary_total_tab(self):
        self.my_dreams.click()
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
        self.driver.switch_to.window(self.diary_window)
        print(self.driver.current_url)
        assert "dreams-diary.html" in self.driver.current_url, "Dream Diary page did not open"
        self.driver.switch_to.window(self.total_window)
        print(self.driver.current_url)
        assert "dreams-total.html" in self.driver.current_url, "Dream Total page did not open"


