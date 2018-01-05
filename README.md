# Blockchain Demo

Just a code from the tutorial: [Learn Blockchains by Building One](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)

## Prerequisites
- Python 3.6+
- [pipenv](https://docs.pipenv.org/)
- [HTTPie](https://httpie.org/)
- Install app dependencies by running: `pipenv install`

## Running Application

- In order to start the app, run: `pipenv run python api.py --port 5000`
- If everything is working fine, you should have a server listening on `5000` port

## API Endpoints

Examples provided by calling API using previously mentioned **HTTPie** tool

### Mine a Block
`http GET :5000/mine`

### Creating New Transaction
`http POST :5000/transactions/new sender="someone_rich" recipient="happy_receiver" amount=5`

### View the Chain
`http GET :5000/chain`



