from src.client import FiscaLinkClient

def main():
    print("Initializing FiscaLink FLS-1 Middleware...")
    
    try:
        # Initialize the client (will automatically validate environment variables)
        client = FiscaLinkClient()
        
        # Test Sandbox Connection
        status = client.ping_sandbox()
        print("Sandbox Status:", status)
        
        # Simulate an invoice submission
        sample_invoice = {
            "invoice_number": "INV-1001",
            "amount": 150.00,
            "currency": "USD",
            "tax_rate": 0.15
        }
        
        receipt = client.submit_invoice(sample_invoice)
        print("Transaction Receipt:", receipt)
        
    except ValueError as e:
        print(f"Initialization Failed: {e}")
        print("Please ensure your .env file is configured correctly.")

if __name__ == "__main__":
    main()
