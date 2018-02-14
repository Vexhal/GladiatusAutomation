from functions import puts
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotVisibleException
from selenium.webdriver.support.ui import Select
import time

###########    JOB     ###########

def get_job_menu(client):
  time.sleep(1)
  client.execute_script("switchMenu(1)")
  try:
    return client.find_element_by_css_selector("#submenu1 > a:nth-child(1)")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_job_do(client):
  time.sleep(1)
  try:
    return client.find_element_by_css_selector("#doWork")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False
    
def get_job_cooldown_time(client):
  time.sleep(1)
  try:
    cooldown = client.find_element_by_css_selector(
      "#content > article > section > table > tbody > tr:nth-child(3) > td:nth-child(2) > span")
    nums = [int(n) for n in cooldown.text.split(':')]
    return nums[0] * 3600 + nums[1] * 60 + nums[2]
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

########### DUNGEON ###########

def get_dungeon_cooldown_time(client, check_for_work):
  try:
    cooldown_bar_text = client.find_element_by_css_selector("#cooldown_bar_text_dungeon").text
    if (cooldown_bar_text == "-"):
      return False
    if (check_for_work):
      return True
    nums = [int(n) for n in cooldown_bar_text.split(':')]
    return nums[0] * 3600 + nums[1] * 60 + nums[2]
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_dungeon_points(client):
  try:
    return int(client.find_element_by_css_selector("#dungeonpoints_value_point").text)
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_dungeon_bar(client):
  time.sleep(1)
  try:
    return client.find_element_by_css_selector("#cooldown_bar_dungeon > a:nth-child(3)")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_dungeon_tab(client):
  time.sleep(1)
  try:
    return client.find_element_by_css_selector("#mainnav > li > table > tbody > tr > td:nth-child(2) > a")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False
 
def get_dungeon_dif1(client):
  time.sleep(1)
  try:
    return client.find_element_by_css_selector(
      "#content > div:nth-child(3) > div > form > table > tbody > tr > td:nth-child(1) > input")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False
    
def get_dungeon_areas(client):
  try:
    return client.find_elements_by_css_selector("img[src='9194/img/combatloc.gif']")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False
    
def is_dungeon_on_cooldown(client):
  try:
    return client.find_element_by_css_selector("#content > div:nth-child(2) > div > div > span")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False
 
########### EXPEDITION ###########

def get_points(client):
  try:
    return int(client.find_element_by_css_selector("#expeditionpoints_value_point").text)
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_expedition_bar(client):
  time.sleep(1)
  try:
    return client.find_element_by_css_selector("#cooldown_bar_expedition > a:nth-child(3)")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False
    
def get_location(client, location_selection):
  client.execute_script("switchMenu(2)")
  time.sleep(1)
  puts("Selected {0} location".format(location_selection))
  try:
    return client.find_element_by_css_selector("#submenu2 > a:nth-child({0})".format(str(location_selection)))
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    puts("Cannot select place {0}".format(str(location_selection)))
  return False
  
def get_enemy(client, enemy_selection):
  time.sleep(1)
  puts("Selected {0} enemy".format(enemy_selection))
  try:
    return client.find_element_by_css_selector(
          "div.expedition_box:nth-child({0}) > div:nth-child(2) > button:nth-child(1)".format(str(enemy_selection)))
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    puts("Cannot select enemy {0}".format(str(location_selection)))
  return False
  
def get_expedition_cooldown_time(client, check_for_work):
  try:
    cooldown_bar_text = client.find_element_by_css_selector("#cooldown_bar_text_expedition").text
    if (cooldown_bar_text == "-"):
      return False
    if (check_for_work):
      return  True
    nums = [int(n) for n in cooldown_bar_text.split(':')]
    return nums[0] * 3600 + nums[1] * 60 + nums[2]
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False
    
def is_expedition_on_cooldown(client):
  try:
    cooldown_indicator = client.find_elements_by_class_name("expedition_cooldown_reduce")
    if(len(cooldown_indicator) > 0):
      return True
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False
    
    
####### LOG IN #########
def get_username_box(client):
  time.sleep(1)
  try:
    return client.find_element_by_id("login_username")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False
    
def get_password_box(client):
  try:
    return client.find_element_by_id("login_password")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_server_box(client):
  try:
    return Select(client.find_element_by_id("login_server"))
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

    
#### CHARACTER ####

def get_tab(client,tab_index):
  try:
    return client.find_element_by_css_selector(
      "#inventory_nav > a:nth-child({0})".format(tab_index))
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_inventory(client):
  try:
    return client.find_element_by_id("inv")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_avatar(client):
  time.sleep(1)
  try:
    return client.find_element_by_css_selector("#avatar > div:nth-child(4)")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_current_hp_percentage(client):
  time.sleep(1)
  try:
    return int(client.find_element_by_id("header_values_hp_percent").text[:-1])
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False
    
def get_character_view(client):
  time.sleep(1)
  try:
    return client.find_element_by_css_selector("#mainmenu > a:nth-child(1)")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

#### ARENAS ####

def is_arena_provinciarum_on_cooldown(client):
  try:
    cooldown_indicator = client.find_elements_by_css_selector("#errorText > span")
    if(len(cooldown_indicator) > 0):
      return True
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_arena_provinciarum_enemy(client, enemy_selection):
  time.sleep(1)
  puts("Selected {0} enemy".format(enemy_selection))
  try:
    return client.find_elements_by_class_name("attack")[enemy_selection-1]
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    puts("Cannot select enemy {0}".format(str(location_selection)))
  return False

def get_arena_provinciarum_tab(client):
  time.sleep(1)
  try:
    return client.find_element_by_css_selector(
       "#mainnav > li:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_arena_bar(client):
  try:
    return client.find_element_by_css_selector("#cooldown_bar_arena > a:nth-child(3)")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_arena_cooldown_time(client, check_for_work):
  try:
    cooldown_bar_text = client.find_element_by_css_selector("#cooldown_bar_arena").text
    if (cooldown_bar_text == "-"):
      return False
    if (check_for_work):
      return  True
    nums = [int(n) for n in cooldown_bar_text.split(':')]
    return nums[0] * 3600 + nums[1] * 60 + nums[2]
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False    

#### NOTIFICATIONS ####

def get_bonus(client):
  try:
    return client.find_element_by_id("linkLoginBonus")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False

def get_notification(client):
  try:
    return client.find_element_by_id("linknotification")
  except (NoSuchElementException, ElementNotVisibleException,ElementNotVisibleException):
    return False