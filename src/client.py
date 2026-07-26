import requests
import json
import time
from src.config import Config
from src.crypto import SignatureManager

class FiscaLinkClient:
    """Primary client for virtual fiscalisation API integration."""
    
    def __init__(self):
        Config.validate()
        self.device_id = Config.DEVICE_ID
        self.activation_key = Config.ACTIVATION_KEY
        self.base_url = Config.BASE_URL

    def _build_headers(self, payload_str: str = "") -> dict:
        """Constructs secure headers with cryptographic signatures."""
        headers = {
            "Device-ID": self.device_id,
            "Content-Type": "application/json",
            "Timestamp": str(int(time.time()))
        }
        if payload_str:
            signature = SignatureManager.generate_signature(payload_str, self.activation_key)
            headers["X-Signature"] = signature
            
        return headers

    def heartbeat(self):
        """Sends a keep-alive ping to the tax authority servers."""
        url = f"{self.base_url}/system/heartbeat"
        print(f"Sending heartbeat to {url}...")
        # Simulated response
        return {"status": "online", "server_time": time.time()}

    def register_device(self):
        """Registers the virtual fiscal device for the first time."""
        url = f"{self.base_url}/device/register"
        payload = json.dumps({"device_id": self.device_id, "model": "FLS-1 Virtual"})
        headers = self._build_headers(payload)
        
        print("Registering fiscal device...")
        # Simulated response
        return {"status": "success", "fiscal_code": "FSC-001-TEST"}

    def submit_invoice(self, invoice_data: dict):
        """Signs and submits a standard sales invoice."""
        url = f"{self.base_url}/invoices/submit"
        payload_str = json.dumps(invoice_data)
        headers = self._build_headers(payload_str)
        
        print(f"Submitting securely signed invoice payload...")
        # Simulated transmission
        return {"status": "success", "receipt_id": "FISCA-9982-TEST", "fiscal_hash": "A8F9B2..."}

    def submit_credit_note(self, original_receipt_id: str, refund_data: dict):
        """Submits a credit note to reverse or refund a previous transaction."""
        url = f"{self.base_url}/invoices/credit-note"
        payload_str = json.dumps({
            "original_receipt": original_receipt_id,
            "refund_details": refund_data
        })
        headers = self._build_headers(payload_str)
        
        print(f"Processing credit note for receipt {original_receipt_id}...")
        return {"status": "success", "credit_note_id": "CN-5541-TEST"}

    def generate_z_report(self):
        """Requests the daily Z-Report (End of Day closure)."""
        url = f"{self.base_url}/reports/z-report"
        headers = self._build_headers()
        
        print("Closing day and generating Z-Report...")
        return {"status": "success", "total_sales": 150.00, "total_tax": 22.50}
