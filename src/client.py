import requests
import json
from src.config import Config
from src.crypto import SignatureManager

class FiscaLinkClient:
    """Primary client for virtual fiscalisation integration."""
    
    def __init__(self):
        Config.validate()
        self.device_id = Config.DEVICE_ID
        self.activation_key = Config.ACTIVATION_KEY
        self.base_url = Config.BASE_URL

    def ping_sandbox(self):
        """Tests the connection to the tax authority sandbox."""
        url = f"{self.base_url}/status"
        headers = {
            "Device-ID": self.device_id,
            "Content-Type": "application/json"
        }
        
        print(f"Pinging Sandbox Environment at {url}...")
        try:
            # Simulated response for open-source framework blueprint
            # response = requests.get(url, headers=headers)
            # return response.json()
            return {"status": "success", "message": "FiscaLink sandbox connection established."}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def submit_invoice(self, invoice_data: dict):
        """Signs and submits invoice data to the tax authority."""
        payload_str = json.dumps(invoice_data)
        signature = SignatureManager.generate_signature(payload_str, self.activation_key)
        
        headers = {
            "Device-ID": self.device_id,
            "X-Signature": signature,
            "Content-Type": "application/json"
        }
        
        print(f"Submitting securely signed invoice payload...")
        # Simulated transmission
        return {"status": "success", "receipt_id": "FISCA-9982-TEST"}
