class Factoriser:

    def __init__ (self):
        self.factoriser = 'Factoriser'

    def do_maths(self):

        n  = orig = prompt('Give me a composite number?');
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        if len(factors) - 1:
            alert('Thanks. ' + orig + 's prime factors are: ' + factors);
        else:
            alert('You gave a prime, duh')

factoriser = Factoriser()
