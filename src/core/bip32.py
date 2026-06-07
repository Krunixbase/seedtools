class BIP32:
    def derive(self, seed: bytes, path: str) -> dict:
        """
        Deterministically derive a key from seed and BIP32 path.
        Returns:
            {
                "private_key": bytes,
                "public_key": bytes,
                "chain_code": bytes,
                "path": str
            }
        """
        raise NotImplementedError
