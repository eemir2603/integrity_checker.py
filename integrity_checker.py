import hashlib

def hash_calculate(metin):
    # It encrypts the text using the SHA-256 algorithm and extracts its hash.
    return hashlib.sha256(metin.encode('utf-8')).hexdigest()

# 1st Stage: Orijinal Data
orijinal_text = "CIA Triad is so important in cybersecurity."
orijinal_hash = hash_calculate(orijinal_text)

print(f"Orijinal Mesaj: {orijinal_text}")
print(f"Orijinal SHA-256 Hash: {orijinal_hash}\n")

# 2nd Stage: Attacking the Data (Some changes in the word of 'triad')  (it could be anything else.. literally anything ;D)
# Word of 'Triad' 'T' goes to 't'  
manipule_text = "CIA triad is so important in cybersecurity."
manipule_hash = hash_calculate(manipule_text)

print(f"Manipule Text: {manipule_text}")
print(f"Manipule SHA-256 Hash: {manipule_hash}\n")

# 3rd Stage:  Integrity Control
if orijinal_hash == manipule_hash: 
    print("[SECURED] Data integrity is intact, no changes have been made so far..")
else:
    print("[!DANGER!] Data integrity is broken, It has been attacked!!")