from pyredictit.pyredictit import pyredictit

pyredictit_api = pyredictit()
pyredictit_api.create_authed_session(username='YOUR_USERNAME',
                                     password='YOUR_PASSWORD')
pyredictit_api.get_my_contracts()
pyredictit_api.list_my_contracts()

>>>------
>>>2017-01-23 16:50:07.667045
>>>Will Donald Trump post 35 - 39 tweets from Jan. 18 - 25?
>>>35 - 39
>>>You have 5 Yes shares.
>>>Your shares have gained +$0.15 in value.
>>>Your average purchase price of Yes shares is 33¢
>>>Yes shares are currently being sold at 36¢
>>>Yes shares are currently being bought for 35¢
>>>If you sold all of your shares now, you would earn $0.1
>>>The implied odds of this contract resolving to Yes are 36%
>>>If this contract resolves to Yes, you would earn $0.1. Otherwise, you would lose $-1.8}
>>>------
