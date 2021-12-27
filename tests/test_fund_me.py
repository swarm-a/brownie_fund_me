from brownie import network, accounts, exceptions
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    poa_compatibility_check,
)
from scripts.deploy import deploy_fund_me
import pytest


def test_can_fund_and_withdraw():
    poa_compatibility_check()
    account = get_account()
    fund_me = deploy_fund_me()
    print(fund_me.getPrice())
    entrance_fee = fund_me.getEntranceFee() + 100
    print(
        f"The current entrance fee is {entrance_fee} wei ({entrance_fee/(10**18)} eth)"
    )
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    # poa_compatibility_check()
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
