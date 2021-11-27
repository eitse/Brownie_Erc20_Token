from web3 import Web3
from brownie import OurToken
from scripts.helpful_scripts import get_account


def deploy_OurToken():
    account = get_account()
    initial_supply = Web3.toWei(1000, "ether")
    our_token = OurToken.deploy(initial_supply, {"from": account})
    print(our_token.name())


def main():
    deploy_OurToken()
