# funzione senza argomenti né valore di ritorno
def print_ciao():
    print("ciao mondo")

# funzione con argomenti e senza valore di ritorno
def somma( a, b ):
    print( a + b )

# funzione con argomenti e valore di ritorno
def rsomma( a, b ):
    return a + b

# funzione con valore di default per un argomento
def pciao( nome = "mondo" ):
    print( "ciao " + nome )
