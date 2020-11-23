# facebook_autocomment

The Script is Written with Python-Selenium.
Download the Source. 
and Download WebDriver(Chrome/Firefox) for Your OS.
Make Sure You placed your WebDriver in "drivers" Folder.
else edit path from "root/fb/fbcomment.py" [line: 39 for Chrome WebDriver] & [line: 41: for Firefox WebDriver].
install requirements.
Edit main.py with your informations like Post URL, List of Comments, How many comments you want to make Etc.
and Run "main.py".

[N.B. WebDrivers Used here is for Windows 64bit OS. Download Your version.]

Links to some of the more popular browser drivers follow.

Chrome:	    https://sites.google.com/a/chromium.org/chromedriver/downloads

Firefox:	  https://github.com/mozilla/geckodriver/releases

Edit/Write "main.py" like,

    from fb.fbcomment import Client
    class Bot(Client):
        pass
    if __name__ == "__main__":
        url = "Post Link"   #Post link
        comments = [        #List of Comments
            'comment0',
            'comment1',
            'comment2',
            'comment3',
            'comment4',
            'comment5',
            'comment6',
            'comment7'
        ]
        bot = Bot("Your Email", "Your Password", 'chrome') #mail, pass, 'chrome'/'firefox' the browser you use!
        bot.commentInFlow(url, comments, 10) 
        bot.close()
