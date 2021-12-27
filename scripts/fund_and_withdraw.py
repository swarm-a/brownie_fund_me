from brownie import FundMe
from brownie.network import account
from scripts.helpful_scripts import get_account, poa_compatibility_check


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(
        f"The current entrance fee is {entrance_fee} wei ({entrance_fee/(10**18)} eth)"
    )
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee + entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing...")
    fund_me.withdraw({"from": account})


def main():
    poa_compatibility_check()
    fund()
    withdraw()


if __name__ == "__main__":
    main()
