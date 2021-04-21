import random

def gcd(x, y):
    
    while x!=y:
        if x>y:
            x = x - y
        else:
            y = y - x

    return x

class CifradorRSA:
    
    def __init__(self):

        self.__list_primes = [2, 3, 5, 7, 11, 13]
        self.p = None
        self.q = None
        self.n = None
        self.__z = None
        self.k = None
        self.__private_key = None
        self.forbidden = True

    def generate_random(self):
        self.p = self.num_prime(random.randrange(100, 200))
        self.q = self.num_prime(random.randrange(100, 200))
        self.n = self.p * self.q
        self.__z = (self.p - 1) * (self.q - 1)
        self.__select_k()
        self.__select_priv_key()

    def Select(self, p, q):
        self.p = p
        self.q = q

        if self.isprime(p) and self.isprime(q):
            self.p = p
            self.q = q
            self.n = self.p * self.q
            self.__z = (self.p - 1) * (self.q - 1)
            self.__select_k()
            self.__select_priv_key()

        else:
            raise ValueError("Numbers in Select method must be primes")

    def __select_k(self):

        for i in range(1, len(self.__list_primes)):

            if gcd(self.__z, self.__list_primes[i]) == 1:
                self.k = self.__list_primes[i]
                break
    
    def __select_priv_key(self):

        for i in range(1, self.__z+1):
            if self.k*i % self.__z == 1:
                self.__private_key = i
                break

    def cifre(self, M):

        return (M**(self.k)) % self.n

    def descifre(self, E):

        return (E**(self.__private_key)) % self.n

    def isprime(self, n):

        if self.__list_primes[-1] >= n:
            if n in self.__list_primes:
                return True
        
        else:

            x = self.__list_primes[-1]+2
            z = 1

            while self.__list_primes[-1]<=n:
                if self.__list_primes[z] > x**(1/2):
                    self.__list_primes.append(x)
                    z = 1
                    x = x+2
                elif x%self.__list_primes[z] != 0:
                    z = z+1
                else:
                    x = x+2
                    z = 1

            if n in self.__list_primes:
                return True

        return False


    def num_prime(self, pos):

        x = self.__list_primes[-1]+2
        z = 1

        while len(self.__list_primes)<pos:

            if self.__list_primes[z] > x**(1/2):
                self.__list_primes.append(x)
                z = 1
                x = x+2
            elif x%self.__list_primes[z] != 0:
                z = z+1
            else:
                x = x+2
                z = 1
        
        return self.__list_primes[pos-1]

    def cifre_message(self, message):

        cif_mes = ""

        for i in range(len(message)):

            if i == len(message)-1:
                cif_mes += str(self.cifre(ord(message[i])))
            else:
                cif_mes += str(self.cifre(ord(message[i]))) + " "

        return cif_mes

    def descifre_message(self, message):

        orig_mes = ""
        message = message.split()

        for i in range(len(message)):
            orig_mes += chr(self.descifre(int(message[i])))

        return orig_mes