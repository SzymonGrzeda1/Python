import tweepy
import pandas as pd

bearer_token        = "AAAAAAAAAAAAAAAAAAAAACPe0gEAAAAAyhPhwoZHj50KJAw69%2FJeR2ESXEM%3DIm07nQfa862EuvAXRdtmkuKtK3pUc4MXfDjmalbUmwh4R2RGnZ"
api_key             = "FrUGN9sqMwpl7xwkSmWUdSARe"
api_secret          = "3N3RrSdULJOm52pG9CukBcyK8fXZGdLWUFunUp3Tj0ICb2ub4d"
access_token        = "1775638873684471808-p2BbpAiHuhS4s3A715dAsovJZXfrmB"
access_token_secret = "RxMBw0Qof4K0f3aU8BE3T7zNF20MHT8pBJpHgokEQ9KjO"
    

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

client.create_tweet(text="Hello Twitter")

