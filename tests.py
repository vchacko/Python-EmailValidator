from EmailValidator import EmailValidator

v = EmailValidator()
assert v
assert v.is_valid('something@gmail.com') is True
assert v.is_valid('something12345678901234567890123456789012345678901234567890123456789012@gmail.com') is False
assert v.is_valid('something12@gmail12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890.com') is False
assert v.is_valid('something12345678901234567890123456789012345678901234567890@12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890gmail.com') is False
assert v.is_valid('something@12#gmail.com') is False
assert v.is_valid('something@12@gmail.com') is False
assert v.is_valid() is False