import pytest
import brownie
from brownie import (
    interface
)
from config import (
    usdc
)

from rich.console import Console
from rich.table import Table

console = Console()

def test_first_deposit(nitroswap, alice):
    '''
    scenario: first deposit 
    1) usdc_minter mints 100 usdc to alice
    2) alice deposits 100 USDC into the MarginPool vault and should receive 
    100 LP tokens as a receipt
    '''
    (margin_pool) = nitroswap

    # deposit
    prevBaseBalAlice = interface.IERC20(usdc).balanceOf(alice)
    prevBaseBalMarginPool = interface.IERC20(usdc).balanceOf(margin_pool)
    prevLpBalAlice = interface.IERC20(margin_pool).balanceOf(alice)

    tx = margin_pool.deposit(100e6, {'from': alice})

    afterBaseBalAlice = interface.IERC20(usdc).balanceOf(alice)
    afterBaseBalMarginPool = interface.IERC20(usdc).balanceOf(margin_pool)
    afterLpBalAlice = interface.IERC20(margin_pool).balanceOf(alice)

    assert prevBaseBalAlice > afterBaseBalAlice
    assert prevBaseBalMarginPool < afterBaseBalMarginPool
    assert prevLpBalAlice < afterLpBalAlice
    assert afterLpBalAlice - prevLpBalAlice == 100e6
    assert afterBaseBalMarginPool - prevBaseBalMarginPool == 100e6
    assert interface.IERC20(margin_pool).totalSupply() == 100e6

    # reporting
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("actor", style="dim", width=12)
    table.add_column("before")
    table.add_column("after")
    table.add_column("diff")
    table.add_row('alice', str(prevBaseBalAlice), str(afterBaseBalAlice), str(prevBaseBalAlice - afterBaseBalAlice))
    table.add_row('margin pool', str(prevBaseBalMarginPool), str(afterBaseBalMarginPool), str(prevBaseBalMarginPool -afterBaseBalMarginPool))
    console.print('[green]CASE: deposit()[/green]')
    console.print(table)




    