import hashlib
import os

PASSWORD = "IETNITK"

print("=" * 120)
print(" "*40 + "PASSWORD HASHING DEMO")
print("=" * 120)
print()
# ===== Plain hash (Unsafe) =====
plain_hash=hashlib.sha256(PASSWORD.encode()).hexdigest()

print("-"*10 + " UNSAFE :- Plain SHA-256 (No salt) " + "-"*10)
print(f"  PASSWORD   :  {PASSWORD}")
print(f"  HASH       :  {plain_hash}")
print("This HASH is same for this PASSWORD\n")

# ===== SHA-256 with first random salt : SAFE =====

salt1=os.urandom(16)                         # 16 cryptographically random bytes
salted_input1= salt1 + PASSWORD.encode()
salted_hash1 = hashlib.sha256(salted_input1).hexdigest()

print("-"*10 + " SAFE :- SHA-256 with random salt (hash 1)" + "-"*10)
print(f"  SALT(hex)  :  {salt1.hex()}")
print(f"  HASH       :  {salted_hash1}"+"\n")

# ===== SHA-256 with second random salt : SAFE =====

salt2=os.urandom(16)                         # 16 cryptographically random bytes
salted_input2= salt2 + PASSWORD.encode()
salted_hash2 = hashlib.sha256(salted_input2).hexdigest()

print("-"*10 + " SAFE :- SHA-256 with different random salt (hash 2)" + "-"*10)
print(f"  SALT(hex)  :  {salt2.hex()}")
print(f"  HASH       :  {salted_hash2}"+"\n")

print("\n" + "=" * 120)
print(" "*50 + "RESULT SUMMARY")
print("=" * 120)
print()
print(f"  Plain hash (same every run) : {plain_hash}")
print(f"  Salted hash #1              : {salted_hash1}")
print(f"  Salted hash #2              : {salted_hash2}")
print(f"\n  Are salted hashes equal?  : {salted_hash1 == salted_hash2}")
print("\nConclusion: The same password produces a DIFFERENT hash each time a fresh salt is used.\n")






