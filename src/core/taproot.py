class TaprootEngine:
    def derive_keypath(self, seed: bytes, path: str) -> dict:
        """
        Deterministic Taproot key-path derivation.
        """
        raise NotImplementedError
