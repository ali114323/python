import webbrowser

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
url = input("Where do you want to go? E.g: google.com ")

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)
