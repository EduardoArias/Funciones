'''Fn - 1
Crear una función que regrese el enésimo número par.
nthPar(1) //=> 0, El primer número par es 0
nthPar(3) //=> 4, El tercer número par es 4 (0, 2, 4)
nthPar(100) //=> 198
nthPar(1298734) //=> 2597466
'''

def  nthPar( n ):
    en = ((n - 1 ) * 2 )
    print ( " Enésimo numero par de " , n, "es " , en)

nthPar(1298734)    