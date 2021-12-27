from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    poa_compatibility_check,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    FORKED_LOCAL_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    active_network = network.show_active()
    # We  need to pass the price feed address to our fundme contract
    print(f"The active network is {network.show_active()}")
    if (
        active_network not in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        and active_network not in FORKED_LOCAL_ENVIRONMENTS
    ):
        price_feed_address = config["networks"][active_network]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][active_network].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    poa_compatibility_check()
    deploy_fund_me()


if __name__ == "__main__":
    main()
