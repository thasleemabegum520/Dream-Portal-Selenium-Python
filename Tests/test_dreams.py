from pages.dreams_diary import DreamsDiary
from pages.dreams_total import DreamsTotal
from pages.mydreams import LoadingAnimation

def test_loading_animation(driver):
    mydreams_obj=LoadingAnimation(driver)
    mydreams_obj.loading_animation()


def test_maincontent_button(driver):
    mydreams_obj = LoadingAnimation(driver)
    mydreams_obj.content_button()

def test_diary_total(driver):
    mydreams_obj = LoadingAnimation(driver)
    mydreams_obj.diary_total_tab()

def test_number_of_dreams(driver):
    dreams_diary_obj= DreamsDiary(driver)
    dreams_diary_obj.num_of_dreams()

def test_dreams_only_good_bad(driver):
    dreams_diary_obj= DreamsDiary(driver)
    dreams_diary_obj.only_good_or_bad()

def test_no_column_empty(driver):
    dreams_diary_obj = DreamsDiary(driver)
    dreams_diary_obj.all_columns_filled()

def test_verify_stats(driver):
    dreams_total_obj=DreamsTotal(driver)
    dreams_total_obj.all_stats()

def test_verify_recurring_dreams(driver):
    dreams_diary_obj = DreamsDiary(driver)
    dreams_diary_obj.recurring_dreams()