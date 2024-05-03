# These two functions will help determine if two numbers are coprimes #
# Returns the greatest common denominator for two numbers
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p
# Determines if two numbers are coprime. Returns True or False
def is_coprime(x, y):
    return gcd(x, y) == 1

# Returns a list of all the prime numbers from 2 to n
def primes_less_than(n):
	all_primes=[]
	prime = [True for i in range(n + 1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p ** 2, n + 1, p):
				prime[i] = False
		p += 1
	prime[0]= False
	prime[1]= False
	# Print all prime numbers
	for p in range(n + 1):
		if prime[p]:
			all_primes.append(p)
	return all_primes

# print("All primes less than 1,000:\n"+str(primes_less_than(999)))



# p = 89
# q = 337
# N = p * q
# T = (p-1)*(q-1)


# potential_es = []
# for i in range(T):
# 	if is_coprime(i, T) == True and is_coprime(i, N) == True and i < T:
# 		potential_es.append(i)
# print("Potential E Values:",potential_es)
# e = 47

# running = True
# i = 0
# d = 0
# while running == True:
# 	if (e * i) % T == 1:
# 		d = i
# 		print(d)
# 		running = False
# 	else: 
# 		i += 1
# d = 17615
# print(N)

# enc = [23413, 4444, 28799, 20456, 22271, 14158, 28799, 22745, 16, 23413, 5994, 22745, 17193, 16, 8711, 16, 26567, 11023, 17600, 282, 536, 20475, 282, 16, 17600, 282, 17600, 536, 20475, 13841, 20456, 16, 536, 20475, 24582, 5994, 13841, 20456, 536, 22271, 28799, 19591, 16, 17600, 16, 4656, 10025, 22745, 22271, 28799, 16, 20456, 10025, 16, 818, 28799, 16, 22745, 28799, 22271, 5298, 10025, 20475, 28799, 13702, 16, 12605, 536, 20456, 14158, 6883, 26567]
# dec = ''
# for num in enc:
# 	dec += str((chr(num**d % N)))
# print(dec)

def calc_N(e, q):
	N = e * q
	return N

def calc_T(p, q):
	T = (p-1)*(q-1)
	return T

def pick_e_d(p, q):
	N = calc_N(p,q)
	T = calc_T(p,q)
	e = 0
	for i in range(T):
		if is_coprime(i, T) == True and is_coprime(i, N) == True and i < T:
			e = i
	i = 0
	d = 0
	running = True
	while running == True:
		if (e * i) % T == 1 and i != e:
			d = i
			running = False
		else: 
			i += 1
	return e, d

def encrypt(N, e, letter):
	letter = ord(letter)
	enc_letter = letter**e % N
	return enc_letter

def encrypt_message(N, e, string):
	enc_message = []
	for letter in string:
		enc_message.append(encrypt(N,e,letter))
	return enc_message

def decrypt(N, d, letter):
	dec_letter = letter**d % N
	dec_letter = chr(dec_letter)
	return dec_letter

def decrypt_message(N, d, list):
	message = ''
	for num in list:
		message += decrypt(N, d, num)
	print(message)

decrypt_message(29993, 17615, encrypt_message(29993, 47, "Man this is so crazy"))
print(pick_e_d(3,7))