import pyotp
import time

totp = pyotp.TOTP('base32secret3232')
now = totp.now()

print("TOTP now: ", now)
# OTP verified for current time

result = totp.verify(now)
print(f"Verify [{now}]: {result}")

print("Sleeping for 30sec...")
time.sleep(30)

result_2 = totp.verify(now)
print(f"Verify [{now}]: {result_2}")


