# Broker Central

All in one API to interact with many different brokers

### Current Supported brokers
- TD Ameritrade
- E*Trade
- Tradier

### Planned Additions
- Robinhood
- Webull
- M1 Finance
- Charles Schwab

## Installation (MacOS/Linux)

1. **Install Anaconda**
```console
brew install --cask anaconda
```
Point your terminal to the anaconda installation by opening your ~/.zshrc file and adding this line at the top:
```console
export PATH="/usr/local/anaconda3/bin:$PATH"
```
Then run
```console
source ~/.zshrc
```
2. **Create the python environment**
```console
conda create -n brokercentral python=3.7
conda activate brokercentral
```
> This is where we will install all of our dependencies and what the application will eventually point to. Every time you want to make changes or train run conda activate

3. **Install dependencies**
```console
pip install -r requirements.txt
brew cask install chromedriver
```

4. **Setup API**
```console
python setup.py
```
Instructions to set up developer accounts
### TDA
### E*Trade
### Tradier

## To Do
Feel free to create pull request with any additional features
- Create broker agnostic api
- Add other brokers
