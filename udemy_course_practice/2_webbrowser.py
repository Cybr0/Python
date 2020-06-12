import webbrowser
url = 'https://djbook.ru/rel3.0/intro/tutorial01.html'
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
webbrowser.get('Chrome').open_new_tab(url)
