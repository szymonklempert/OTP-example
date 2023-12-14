import pyotp
from qrcode.main import QRCode
import time

totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
url = pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name='test@google.com', issuer_name='Secure App')

qr = QRCode()
qr.add_data(data=url)
qr.print_ascii()

time.sleep(10)

while(True):
    print("Current OTP:", totp.now())
    time.sleep(1)