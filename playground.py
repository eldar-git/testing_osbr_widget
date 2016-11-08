# -*- coding: cp1251 -*-
#import pytest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException        

# help fuction, checking the existance of an element
def check_exists_by_css(css_path):
    try:
        driver.find_element_by_css_selector(css_path)
    except NoSuchElementException:
        return False
    return True

driver = webdriver.Chrome('C:/Users/eldar/Desktop/selenium_test/chromedriver') # !!! change the path to location of the chromedrive.exe 
#driver.maximize_window()
driver.get("http://www.sberbank.ru/ru/person")

#widget = driver.find_element_by_css_selector('[data-pid="personalRates"]')
#widget = driver.find_element_by_css_selector('div[class="bp-widget aa-widget personalized-widget bp-ui-dragRoot"]' and 'div[data-pid="personalRates"]')
widget = driver.find_element_by_css_selector('.bp-widget.aa-widget.personalized-widget.bp-ui-dragRoot')
#widget = driver.find_element_by_css_selector('div[data-pid="personalRates"]')
widgetHead = driver.find_element_by_css_selector('.bp-widget-head.personalized-widget-head.bp-ui-dragGrip')
widgetTitle = driver.find_element_by_css_selector('.personalized-widget-title.aa-widget-head-draggable.rates-icon')
widgetTitleIcons = driver.find_element_by_css_selector('.widget-icons')
widgetTitleIconHider = driver.find_element_by_css_selector('.widget-icon-hider')
widgetTitleIconToAccessWidgetCatalog = driver.find_element_by_css_selector('[class="catalog-w"]' and '[data-action="sbrf-widget-catalog"]')
widgetTitleIconMinimizeWidget = driver.find_element_by_css_selector('[class="catalog-w"]' and '[data-action="widget-minimize"]')
widgetBody = driver.find_element_by_css_selector('.bp-widget-body')
widgetCurrencySectionBoby = driver.find_element_by_css_selector('a[class="currency-section currency"]')
widgetMetalSectionName = driver.find_element_by_css_selector('li[data-type="metal"]')


### CHECKING IF THE WIDGET IS LOADED ###########################################


#assert widget.is_displayed(), "widget is not visible"
#assert widgetHead.is_displayed(), "widget head is not visible"
#assert widgetTitle.is_displayed(), "widget title is not visible"
#assert widgetTitleIconHider.is_displayed(), "widget icon hider is not visible"
#assert widgetCurrencySectionBoby.is_displayed(), "widget body is not visible"


### CHECKING THE CYCLE OF OPEN/CLOSE THE WIDGET CATALOG ########################


## checking if the widget's additional icons are visible
#if widgetTitleIcons.is_displayed():
#    
#    assert widgetTitleIconToAccessWidgetCatalog.is_displayed(), "the catalog switching icon is not visible"
#    
#    # clicking on widget catalog opener icon
#    widgetTitleIconToAccessWidgetCatalog.click()
#    
#    # appearance of the widget's back
#    widgetBack = driver.find_element_by_css_selector('div[class="sbrf-widget-catalog"]')
#    
#    assert widgetBack.is_displayed(), "the widget catalog is not displayed"
#    
#    # closing widget catalog on the widget's back and returning back to initial widget
#    widgetBackCloseIcon = driver.find_element_by_css_selector('[class="close-icon"]')
#    
#    assert widgetBackCloseIcon.is_displayed(), "the close icon is not displayed"    
#    
#    widgetBackCloseIcon.click()
#    
#    assert not check_exists_by_css('[class="flip-container goFlip"]'), "the widget is not flipped back to initial state"
#    
#else:
#    
#    # clicking on icon hider to open additional icons
#    widgetTitleIconHider.click()
#    
#    assert widgetTitleIconToAccessWidgetCatalog.is_displayed(), "the catalog switching icon is not visible"
#    
#    # clicking on widget catalog opener icon
#    widgetTitleIconToAccessWidgetCatalog.click()
#    
#    # appearance of the widget's back
#    widgetBack = driver.find_element_by_css_selector('div[class="sbrf-widget-catalog"]')
#    
#    assert widgetBack.is_displayed(), "the widget catalog is not displayed"
#    
#    # closing widget catalog on the widget's back and returning back to initial widget
#    widgetBackCloseIcon = driver.find_element_by_css_selector('a[class="close-icon"]')
#    
#    assert widgetBackCloseIcon.is_displayed(), "the close icon is not displayed"
#    
#    widgetBackCloseIcon.click()
#    
#    assert not check_exists_by_css('[class="flip-container goFlip"]'), "the widget is not flipped back to initial state"


### CHECKING THE OPTION OF SWITCHING TO ANOTHER WIDGET #########################


## checking if the widget's additional icons are visible
#if widgetTitleIcons.is_displayed():
#    
#    assert widgetTitleIconToAccessWidgetCatalog.is_displayed(), "the catalog switching icon is not visible"
#    
#    # clicking on widget catalog opener icon
#    widgetTitleIconToAccessWidgetCatalog.click()
#    
#    # appearance of the widget's back
#    widgetBack = driver.find_element_by_css_selector('div[class="sbrf-widget-catalog"]')
#    
#    assert widgetBack.is_displayed(), "the widget catalog is not displayed (1st round)"
#    
#    assert driver.find_element_by_css_selector('[data-item-name="SBR_CardChooser"]').is_displayed(), "the item 'Credit Card Choser' is not displayed"
#    
#    #switching to the widget (credit cadrs)
#    driver.find_element_by_css_selector('[data-item-name="SBR_CardChooser"]').click()
#
#    if widgetHead:
#        
#        # clicking on icon to flip widget and access the widget catalog
#        widgetTitleIconToAccessWidgetCatalog.click()
#        
#        widgetBack = driver.find_element_by_css_selector('div[class="sbrf-widget-catalog"]')
#
#        assert widgetBack.is_displayed(), "the widget catalog is not displayed (2nd round)"
#        
#        #switching to the widget (credit cadrs)
#        driver.find_element_by_css_selector('[data-item-name="SBR_CardChooser"]').click()
#        
#    else:
#        
#        pass
#        
#    assert check_exists_by_css('[class="personalized-widget-title aa-widget-head-draggable card-chooser-icon"]'), "the Credit Card Choser widget is not visible"
#    
#else:
#    
#    # clicking on icon hider to open additional icons
#    widgetTitleIconHider.click()
#    
#    assert widgetTitleIconToAccessWidgetCatalog.is_displayed(), "the catalog switching icon is not visible"
#    
#    # clicking on icon to flip widget and access the widget catalog
#    widgetTitleIconToAccessWidgetCatalog.click()
#    
#    # appearance of the widget's back
#    widgetBack = driver.find_element_by_css_selector('div[class="sbrf-widget-catalog"]')
#    
#    #assert widgetBack.is_displayed(), "the widget catalog is not displayed (1st round)"
#    
#    #switching to the widget (credit cadrs)
#    driver.find_element_by_css_selector('[data-item-name="SBR_CardChooser"]').click()
#
#    if widgetHead:
#        
#        time.sleep(1)
#        
#        # clicking on icon to flip widget and access the widget catalog
#        widgetTitleIconToAccessWidgetCatalog.click()
#        
#        widgetBack = driver.find_element_by_css_selector('div[class="sbrf-widget-catalog"]')
#
#        assert widgetBack.is_displayed(), "the widget catalog is not displayed (2nd round)"
#        
#        #switching to the widget (credit cadrs)
#        driver.find_element_by_css_selector('[data-item-name="SBR_CardChooser"]').click()
#        
#    else:
#        
#        pass
#        
#    assert check_exists_by_css('[class="personalized-widget-title aa-widget-head-draggable card-chooser-icon"]'), "the credit card choser widget is not visible"

    
### CHECKING LINK FROM CURRENCY SECTION TO PARTICULAR PAGE #####################


#widgetCurrencySectionBoby.click()
#assert driver.current_url == 'http://www.sberbank.ru/ru/quotes/currenciesbeznal', "the link is not correct"


## CHECKING LINK FROM METAL SECTION TO PARTICULAR PAGE ########################


#widgetMetalSectionName.click()
#time.sleep(1)
#widgetMetalSectionBody = driver.find_element_by_css_selector('[class="currency-section metal"]')
#widgetMetalSectionBody.click()
#assert driver.current_url == 'http://www.sberbank.ru/ru/quotes/metalbeznal', "the link is not correct"


### CHECKING DRAG AND DROP FUNCTIONALITY #######################################

            
#target = driver.find_element_by_css_selector('div[class="sbt-springboard-area-holder col-xs-12 col-sm-6 col-md-3"]')
#ActionChains(driver).drag_and_drop(widget, target).perform()


### CHECKING MINIMIZE WIDGET ICON ##############################################


## checking if the widget's additional icons are visible
#if widgetTitleIcons.is_displayed():
#    
#    # clicking on icon to minimize the widget    
#    widgetTitleIconMinimizeWidget.click()
#    
#    assert not widgetCurrencySectionBoby.is_displayed(), "the widget is not minimized"
#    
#else:
#    
#    # clicking on opions icon to open additional icons
#    widgetTitleIconHider.click()
#    
#    assert widgetTitleIcons.is_displayed(), "the icons are not visible"
#    
#    # clicking on icon to minimize the widget    
#    widgetTitleIconMinimizeWidget.click()
#    
#    assert not widgetCurrencySectionBoby.is_displayed(), "the widget is not minimized"


################################################################################


time.sleep(2)
driver.quit()

#pytest.main()