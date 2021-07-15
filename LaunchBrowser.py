from selenium import webdriver


driver = webdriver.Chrome("C:\\N4\\VSCODE\\SeleniumpythonCode\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/?safe=active&ssui=on")
print(driver.title)
