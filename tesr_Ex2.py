import pytest
from SolutionDebug2 import retrait

def test_retrait ():
    solde=1000
    retrait_1=500
    retrait_2=200
    montant = retrait_1 + retrait_2
    resultat_attendu= solde-(retrait_1+retrait_2)
    resultat_obtenu= retrait(solde,montant)
    assert resultat_obtenu == resultat_attendu

def test_retrait_2 ():
    solde=1000
    retrait_1=700
    retrait_2=400
    montant = retrait_1 + retrait_2
    resultat_attendu= 0
    resultat_obtenu= retrait(solde,montant)
    assert resultat_obtenu == resultat_attendu

def test_retrait_2 ():
    solde=1000
    retrait_1=-100
    retrait_2=0
    montant = retrait_1 + retrait_2
    resultat_attendu= 1000
    resultat_obtenu= retrait(solde,montant)
    assert resultat_obtenu == resultat_attendu