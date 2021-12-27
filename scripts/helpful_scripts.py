from brownie import network, accounts, config, MockV3Aggregator
from web3.middleware import geth_poa_middleware
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = {"mainnet-fork", "mainnet-fork-dev"}
LOCAL_BLOCKCHAIN_ENVIRONMENTS = {"development", "ganache-local"}

DECIMALS = 8
STARTING_PRICE = 4000 * (10 ** 8)


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def poa_compatibility_check():
    poa_flag = False
    for mw in list(network.web3.middleware_onion):
        if "GethPOAMiddleware" in str(mw):
            print("Provider has geth PoA middleware")
            poa_flag = True
            break
    if not poa_flag:
        print("Injecting geth PoA middleware")
        network.web3.middleware_onion.inject(geth_poa_middleware, layer=0)


def deploy_mocks():
    print("Deploying mocks...")
    MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
