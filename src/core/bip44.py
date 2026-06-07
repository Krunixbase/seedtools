class BIP44:
    def derive_account(self, seed: bytes, purpose: int, coin: int, account: int):
        """
        Derive BIP44 account root.
        """
        raise NotImplementedError
