import pyotp

hotp = pyotp.HOTP('base32secret3232')
at_0 = hotp.at(0) # => '260182'
at_1 = hotp.at(1) # => '055283'
at_1401 = hotp.at(1401) # => '316439'

print(f"---HOTP at:---\n0 => {at_0}\n1 => {at_1}\n1401 => {at_1401}")

# OTP verified with a counter
print("--------------")
print("Verify [316439, 1401]:", hotp.verify('316439', 1401))
print("Verify [316439, 1402]:", hotp.verify('316439', 1402))