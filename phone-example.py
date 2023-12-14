import pyotp
import qrcode
import qrcode.image.svg

totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
print("Current OTP:", totp.now())

url = pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name='test@google.com', issuer_name='Secure App')

img = qrcode.make(url, image_factory=qrcode.image.svg.SvgImage)

with open('qr.svg', 'wb') as qr:
    img.save(qr)