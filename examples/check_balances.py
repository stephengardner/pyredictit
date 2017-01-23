from pyredictit.pyredictit import pyredictit

pyredictit_api = pyredictit()
pyredictit_api.create_authed_session(username='YOUR_USERNAME',
                                     password='YOUR_PASSWORD')
pyredictit_api.current_gain_loss()
pyredictit_api.money_invested()
pyredictit_api.money_available()

>>> You've lost $2.26.
>>> You have $39.22 currently invested in contracts.
>>> You have $0.22 available.
