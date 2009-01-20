from multweettwitter.logger import log, DEBUG, ERROR, INFO

from twitter import Twitter


class TwitterPlugin(object):
    """Twitter plugin."""

    max_message_length = 140

    def __init__(self, account):
        self.account = account

    def post_message(self, message):
        options = self.account.options
        twitter = Twitter(options['username'], options['password'])
        log(INFO, 'Posting message to twitter service...')
        result = twitter.statuses.update(status=message)
        log(DEBUG, 'Result is %r', result)
        log(INFO, 'Success!')
