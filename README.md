# Fetch Rewards Backend Engineering Test
### Usage
- This web service runs on Python3 and requires pip libraries: https://www.python.org/downloads/
- Install requirements via `pip3 install -r requirements.txt`
- Run via `python3 app.py`

An example script has been provided for testing: `test.py`
### API

#### POST /transaction
- Adds a transaction for a specific payer and date
- Parameters
  - "payer": string
  - "points": int
  - "timestamp": string
- Returns
  - None
#### POST /spend
- Spends points and returns a list for each call
- Parameters
  - "points": int
- Returns
  - List of payers and their points spent in json
#### GET /balance
- Return all payer point balances
- Parameters
  - None
- Returns
  - Dictionary of payer point balances in json
