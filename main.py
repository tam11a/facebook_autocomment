from fb.fbcomment import Client

class Bot(Client):
    pass

if __name__ == "__main__":

    url = "Post Link"
    comments = [
        'comment0',
        'comment1',
        'comment2',
        'comment3',
        'comment4',
        'comment5',
        'comment6',
        'comment7'
    ]

    bot = Bot("Your Email", "Your Password", 'chrome')
    bot.commentInFlow(url, comments, 10)
    bot.close()
    #--------------- url, comment list and how many comments you want to write
