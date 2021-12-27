from brownie import FundMe
from brownie.network import account
from scripts.helpful_scripts import get_account, poa_compatibility_check
from scripts.deploy import deploy_fund_me
from scripts.fund_and_withdraw import fund, withdraw


def troubleshoot():
    fund_me = FundMe[-1]
    account = get_account()
    print(fund_me.getPrice())
    # entrance_fee = fund_me.getEntranceFee()
    # print(
    #     f"The current entrance fee is {entrance_fee} wei ({entrance_fee/(10**18)} eth)"
    # )
    # print("Funding...")
    # fund_me.fund({"from": account, "value": entrance_fee + entrance_fee})def


def main():
    poa_compatibility_check()
    deploy_fund_me()
    fund()
    # fund()
    withdraw()


if __name__ == "__main__":
    main()
