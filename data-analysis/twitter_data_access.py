from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

consumer_key = 'wEYDVLqQJvJKIfeqcXB6wkqs2'
consumer_secret = 'QXXolFYIqL6IVrAvmli2htjL498aIc4xdSJv3yjE6X8dsHOIkN'
access_token = '1133681938059763713-CROyrAMdrsywpO1XOsEbPQOr4SLZZm'
access_token_secret = 'HZLVIyZQup1PtVc5oRiE5ZWgLALqvCy9zFfcJvvlkAMVs'

auth = OAuthHandler(consumer_key,
                    consumer_secret)

auth.set_access_token(access_token,
                      access_token_secret)

class  PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name,
                  status.created_at,
                  status.source,
                  '\n')

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True #keep stream alive

    def on_timeout(self):
        print('Listener timed out!')
        return True #keep stream alive

def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample(languages=languages)

if __name__ == '__main__':
    print_to_terminal()
