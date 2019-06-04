import numpy as np

# parameters
n = 230 #次元数
q = 2053 #法とする素数
A = np.random.randint(q, size=(n, n)) #nとqから生成される格子の基底
alpha = 8.0 #誤差に関するパラメータ

def randint_from_gaussian(size):
    sigma = alpha/np.sqrt(2*np.pi) #標準偏差α/√2π
    x = np.random.normal(0, sigma, size) #標準偏差α/√2πで正規分布に従った乱数を生成
    return np.rint(x) #小数切り捨て

print('n = ',n,', q = ',q,', alpha = ',alpha,'\nA = ',A,'\n\n')

# keys
s = np.random.randint(q, size=n) #係数（n x 1）
e = randint_from_gaussian(size=n) #誤差（n x 1）
T = (A.dot(s) % q + e) % q #格子点に誤差を加えた点（n x 1）

print('[+] secret key') #秘密鍵の出力
print('s =\n', s)
print('e =\n', e)
print('[+] public key') #公開鍵の出力
print('T =\n', T)

# encryption
plain_bit = 1

r = randint_from_gaussian(size=n)
C1 = r.dot(A) % q
M = (q+1)/2 * plain_bit
C2 = (r.dot(T) - M) % q

print('[+] ciphertext')
print('C1 =\n', C1)
print('C2 =\n', C2)
print("")

# decryption
p = (C1.dot(s) - C2) % q
decrypted_bit = int((q+1)/4 < p < 3*(q+1)/4)
print("[+] decrypted_bit = %d" % decrypted_bit)
