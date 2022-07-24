from multiprocessing.sharedctypes import Value
from typing import Union, Optional, Dict
from .constants import _netname_to_id
from web3 import Web3

class EIP681:
    def __init__(self, chain: Optional[Union[str, int]] = None, address: str = None):
        if chain is not None:
            if type(chain) is str:
                if chain not in _netname_to_id.keys():
                    raise KeyError("Network name not found or not currently supported.")
                self.chain = _netname_to_id[str]
            elif type(chain) is int:
                self.chain = chain
        else:
            # Default to ETH mainnet
            self.chain = 1
        
        self.default_address = address

    def build_tx_url(
        self,
        target: str, 
        payment: bool = False,
        amount: Optional[float] = None, 
        function: Optional[str] = None, 
        params: Optional[Dict[str,str]] = None) -> str:

        if Web3.isAddress(target) == False:
            raise TypeError("target must be valid eth address")

        # target_address = Web3.toChecksumAddress(target)
        
        if amount is not None:
            value = str(amount)+'e18'

        if payment:
            prefix = 'pay-'
            if amount is None:
                raise ValueError("must specify amount of ETH if making payment request")
        else:
            prefix = 'ethereum:'
            if function is None and amount is None:
                raise ValueError("must specify amount of ETH if making payment request")
        
        if function is not None:
            param_string = ''
            for i, (k,v) in enumerate(params):
                param_string+=k+'='+v

            url = f'ethereum:{target}@{self.chain}/{function}?{param_string}'
            return url
        
        url = f'{prefix}{target}@{self.chain}?value={value}'
    
        return url

