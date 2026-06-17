from Crypto.Util.number import long_to_bytes

# Function to calculate the gcd and modular inverse using extended Euclied algorithm
def gcd_extended(a,b):
    if a == 0 :
        return b,0,1
    
    gcd_value,x1,y1=gcd_extended(b%a,a)

    x=y1-x1*((b//a))
    y=x1

    return gcd_value,x,y


# Function to calculate the modular inverse of e 
def mod_inverse(e,phi):
    gcd_val,mod_inverse_value,_=gcd_extended(e,phi)

    return mod_inverse_value % phi


# Function to encrypt the message 

def encrypt_message(message,e,N):
    # Convert the string to raw bytes 
    message_bytes = message.encode("utf-8")

    # Convert the entire byte array to one single number
    M = int.from_bytes(message_bytes, byteorder="big")

    if M >= N:
        raise ValueError("Message too large for the RSA modulus N")
    
    # Encrypt the single big integer
    C = pow(M, e, N)
    return C


# Function to decrypt the cipher_text
def decypt_cipher_text(ciphertext_int, d, N):

    # Decrypt the ciphertext integer back into the original large integer M
    M = pow(ciphertext_int, d, N)

    # Convert the large integer back into raw bytes
    message_bytes = long_to_bytes(M)

    # Decode the bytes back into a readable string
    return message_bytes.decode("utf-8")


# Function to generate keys
def generate_keys():
    # Choose two distinct small prime numbers
    p=999999999999999877
    q=999999999999999613

    # Calculate N
    N=p*q

    # Calculate Euler's totient function phi(n)
    phi=(p-1)*(q-1)

    # Choose e such that 1 < e < phi(n) and gcd(e,phi) = 1   , e = 65537 is a standard value
    e=65537
    
    # Calculate d , which is the modular inverse of e
    d=mod_inverse(e,phi)   

    return p,q,N,phi,e,d


if __name__ == "__main__":

    p,q,N,phi,e,d = generate_keys()

    print("="*50)
    print(" "*15 + "RSA KEY GENERATION" + " "*15 )
    print("="*50)
    print(f"Prime number p : {p}")
    print(f"Prime number q : {q}")
    print(f"N (p*q)        : {N} ( PUBLIC KEY)")
    print(f"e             : {e} ( PUBLIC KEY)")
    print(f"phi(n)        : {phi}")
    print(f"d            : {d} ( PRIVATE KEY)\n")

    message = "Hello , NITK !"
    print(f"Original message   : {message}")

    ciphertext_int=encrypt_message(message,e,N)
    print(f"Encrypted Value    : {ciphertext_int}")

    decrypted_message= decypt_cipher_text(ciphertext_int, d, N)
    print(f"Decrypted messag   : {decrypted_message}")

