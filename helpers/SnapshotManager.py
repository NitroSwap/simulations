from brownie import (
    interface
)
from rich.console import Console
from rich.table import Table

console = Console()

class SnapshotManager:
    def __init__(self, actors, addresses, assets):
        assert len(actors) == len(addresses)

        self.actors = actors
        self.addresses = addresses
        self.assets = assets
        self.table = Table(show_header=True, header_style="bold magenta")

        self.table.add_column("actor", style="dim", width=12)
        self.table.add_column("before")
        self.table.add_column("after")
        self.table.add_column("diff")

    def snap(self):
        assets = []
        for x in self.assets:
            balances = []
            for i in range(len(self.actors)):
                bal = interface.IERC20(x).balanceOf(self.addresses[i])
                balances.append(bal)
            assets.append(balances)
        return assets
            

    def publish(self, before, after):
        assert len(before) == len(after)
        for x in range(len(before)):
            self.table.add_row(self.assets[x], '', '', '')
            for y in range(len(self.actors)):
                self.table.add_row(self.actors[y], str(before[x][y]), str(after[x][y]), str(after[x][y] - before[x][y]))
        console.print(self.table)
            

        


