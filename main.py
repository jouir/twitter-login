#!/usr/bin/env python3
from urllib.parse import urlparse

import argparse
import tweepy
import logging


logger = logging.getLogger(__name__)


def main():

    parser = argparse.ArgumentParser()    
    parser.add_argument('-d', '--debug', dest='loglevel', action='store_const', const=logging.DEBUG,
                        default=logging.INFO, help='print more output')
    parser.add_argument('--consumer-key', help='twitter consumer key', required=True)
    parser.add_argument('--consumer-secret', help='twitter consumer secret', required=True)
    args = parser.parse_args()

    logging.basicConfig(format='%(message)s', level=args.loglevel)

    auth = tweepy.OAuthHandler(args.consumer_key, args.consumer_secret)

    try:
        redirect_url = auth.get_authorization_url()
        logger.info(f'Please go to {redirect_url}')
    except tweepy.TweepError as err:
        logger.error('Cannot get request token')
        logger.debug(str(err))
        return

    token = urlparse(redirect_url).query.split('=')[1]

    try:
        verifier = input('Code: ')
    except KeyboardInterrupt:
        return

    auth.request_token = {'oauth_token': token, 'oauth_token_secret': verifier}

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError as err:
        logger.error('Cannot get access token')
        logger.debug(str(err))
        return

    access_token = auth.access_token
    access_token_secret = auth.access_token_secret

    logger.info('Generated tokens:')
    logger.info(f'ACCESS_TOKEN = {access_token}')
    logger.info(f'ACCESS_TOKEN_SECRET = {access_token_secret}')


if __name__ == '__main__':
    main()
