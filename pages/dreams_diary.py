from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DreamsDiary:
    def __init__(self,driver):
        self.driver = driver
        my_dreams = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "dreamButton")))
        my_dreams.click()
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
        self.driver.switch_to.window(self.diary_window)


    def num_of_dreams(self):
        dream_entries = self.driver.find_elements(By.CSS_SELECTOR, "#dreamsDiary tbody tr")
        assert len(dream_entries) == 10, "Dreams are not 10"

    def only_good_or_bad(self):
        print(self.driver.current_url)
        self.dream_types = WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@id='dreamsDiary']//tbody//tr//td[3]")))
        print(self.dream_types)
        for dream_type in self.dream_types:
            print(dream_type.text)
            assert dream_type.text in ['Good', 'Bad'], "Dream type are neither good nor bad"

    def all_columns_filled(self):
        dreams = self.driver.find_elements(By.XPATH, "//table[@id='dreamsDiary']//tbody//tr//td")
        for cell in dreams:
            assert cell.text != '', "cell has empty field"

    def recurring_dreams(self):
        dreams = self.driver.find_elements(By.XPATH, "//table[@id='dreamsDiary']//tbody//tr//td[1]")
        dream_names=[dream.text for dream in dreams]
        rec_dream=set()
        for dream in dream_names:
            if dream_names.count(dream)>1:
                rec_dream.add(dream)
        for dream in rec_dream:
            print(dream," is recurring")
            assert dream in ['Flying over mountains','Lost in maze'],"Recurring dreams are different"


