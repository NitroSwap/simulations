import pytest
from brownie import (
    accounts,
    interface,
    MarginPool
)
from config import (
    badger,
    usdc,
    name,
    symbol,
    decimals,
    usdc_minter

)
from rich.console import Console

console = Console()

@pytest.fixture(scope="module", autouse=True)
def deployer():
    return accounts[0]

@pytest.fixture(scope="module", autouse=True)
def alice():
    return accounts[1]

@pytest.fixture(scope="module", autouse=True)
def bob():
    return accounts[2]

@pytest.fixture(scope="module", autouse=True)
def bot():
    return accounts[3]

@pytest.fixture(scope="module", autouse=True)
def nitroswap(deployer, alice):

    # deploy
    margin_pool = deploy_margin_pool(badger, usdc, name, symbol, decimals, deployer)

    # wireup
    wireup(alice, margin_pool)

    return (margin_pool)

def deploy_margin_pool(badger, usdc, name, symbol, decimals, dev):
    margin_pool_instance = MarginPool.deploy(badger, usdc, name, symbol, decimals, {"from": dev})
    console.print("[green]Margin Pool was deployed at: [/green]", margin_pool_instance.address)
    return margin_pool_instance

def wireup(alice, margin_pool):
    # mint 100 usdc for alice and approve margin_pool
    tx = interface.IERC20(usdc).mint(alice, 100e6, {'from': usdc_minter})
    assert interface.IERC20(usdc).balanceOf(alice) == 100e6

    tx = interface.IERC20(usdc).approve(margin_pool.address, 100e6, {'from': alice})
    assert interface.IERC20(usdc).allowance(alice, margin_pool.address) == 100e6

## Forces reset before each test
@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass