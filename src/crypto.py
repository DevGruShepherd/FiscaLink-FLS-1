import hashlib
import hmac

class SignatureManager:
    """Handles cryptographic signing for tax authority payloads."""
    
    @staticmethod
    def generate_signature(payload: str, secret_key: str) -> str:
        """
        Generates an HMAC-SHA256 signature for the given payload.
        """
        encoded_payload = payload.encode('utf-8')
        encoded_key = secret_key.encode('utf-8')
        
        signature = hmac.new(encoded_key, encoded_payload, hashlib.sha256).hexdigest()
        return signature
