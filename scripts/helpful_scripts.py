from brownie import network, accounts, config

LOCAL_ENVIRONMENT = ["development", "ganache_local"]
FORK_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev", "mainnet-fork-dev2"]


def get_account():

    if (
        network.show_active() in LOCAL_ENVIRONMENT
        or network.show_active() in FORK_ENVIRONMENT
    ):
        return accounts[0]
    else:
        # Wallet uses MetaMask Private_key
        return accounts.add(config["wallets"]["from_key"])
