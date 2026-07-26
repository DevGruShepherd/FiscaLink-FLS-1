import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    """Central configuration for FiscaLink FLS-1."""
    DEVICE_ID = os.getenv("FISCALINK_DEVICE_ID", "[REDACTED_DEVICE_ID]")
    ACTIVATION_KEY = os.getenv("FISCALINK_ACTIVATION_KEY", "[REDACTED_ACTIVATION_KEY]")
    BASE_URL = os.getenv("TAX_AUTHORITY_SANDBOX_URL", "https://sandbox.taxauthority.gov/api/v1")

    @classmethod
    def validate(cls):
        if cls.DEVICE_ID == "[REDACTED_DEVICE_ID]" or not cls.DEVICE_ID:
            raise ValueError("Configuration Error: FISCALINK_DEVICE_ID is missing.")
        if cls.ACTIVATION_KEY == "[REDACTED_ACTIVATION_KEY]" or not cls.ACTIVATION_KEY:
            raise ValueError("Configuration Error: FISCALINK_ACTIVATION_KEY is missing.")
