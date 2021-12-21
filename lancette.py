"""
Il file contiene funzioni che permettono la costruzione delle lancette di un
orologio.
In particolare le funzioni permettono di:
- creare le lancette delle ore e dei minuti
- creare la lancetta dei secondi
"""
from img_lib_v0_6 import(
    Immagine, 
    affianca, 
    cerchio, 
    rettangolo, 
    ruota,  
    cambia_punto_riferimento,  
    larghezza_immagine,
    altezza_immagine,
)

from testing_util import(
    controlla_valore_atteso
)

RAGGIO = 300
NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
GRIGIO = (84, 84, 84)
ROSSO = (255, 0, 0)
ALTEZZA_LANCETTA_MINUTI = RAGGIO * 10 // 100
LUNGHEZZA_TESTA_LANCETTA_MINUTI = RAGGIO * 20 // 100
LUNGHEZZA_CODA_LANCETTA_MINUTI = RAGGIO * 85 // 100
ALTEZZA_LANCETTA_ORE = RAGGIO * 12 // 100
LUNGHEZZA_LANCETTA_TESTA_ORE = RAGGIO * 20 // 100
LUNGHEZZA_LANCETTA_CODA_ORE = RAGGIO * 60 // 100
ALTEZZA_LANCETTA_SECONDI  = RAGGIO * 2 // 100
RAGGIO_PALLINO_ROSSO = RAGGIO * 8 // 100
LUNGHEZZA_LANCETTA_TESTA_SECONDI = RAGGIO * 25 // 100
LUNGHEZZA_LANCETTA_CODA_SECONDI = RAGGIO * 60 // 100
def crea_lancetta_minuti(angolo: int) -> Immagine:
    """
    Crea la lancetta dei minuti in posizione ore 0
    
    :param angolo: angolo di apertura della lancetta
    :returns: una lancetta ruotata
    """
    posizione_zero = 90
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(LUNGHEZZA_TESTA_LANCETTA_MINUTI, ALTEZZA_LANCETTA_MINUTI, NERO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(LUNGHEZZA_CODA_LANCETTA_MINUTI, ALTEZZA_LANCETTA_MINUTI, NERO)), 
        "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, posizione_zero)
    return ruota(lancetta_verticale, -(angolo))

controlla_valore_atteso(larghezza_immagine(crea_lancetta_minuti(90)), LUNGHEZZA_TESTA_LANCETTA_MINUTI + LUNGHEZZA_CODA_LANCETTA_MINUTI)
controlla_valore_atteso(altezza_immagine(crea_lancetta_minuti(90)), ALTEZZA_LANCETTA_MINUTI)


def angolo_minuti(minuti: int) -> int:
    """
    Definisce il grado di rotazione rispetto ai minuti
    
    :param minuti: la posizione della lancetta
    :returns: l'angolo di apertura della lancetta rispetto alla posizione 0
    """
    grado_rotazione_minuto = 360 // 60
    return minuti * grado_rotazione_minuto


def crea_lancetta_ore(angolo: int) -> Immagine:
    """
    Crea l'immagine di una lancetta in posizione 0
    
    :params angolo: angolo di rotazione rispetto alla posizione 0
    :returns: una lancetta ruotata
    """
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(LUNGHEZZA_LANCETTA_TESTA_ORE, ALTEZZA_LANCETTA_ORE, NERO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(LUNGHEZZA_LANCETTA_CODA_ORE, ALTEZZA_LANCETTA_ORE, NERO)), 
        "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    return ruota(lancetta_verticale, -(angolo))

controlla_valore_atteso(larghezza_immagine(crea_lancetta_ore(90)), LUNGHEZZA_LANCETTA_TESTA_ORE + LUNGHEZZA_LANCETTA_CODA_ORE)
controlla_valore_atteso(altezza_immagine(crea_lancetta_ore(90)), ALTEZZA_LANCETTA_ORE)


def angolo_ore(ore: int, minuti: int) -> int:
    """
    Definisce il grado di rotazione della lancetta delle ore rispetto alle ore
    e ai minuti
    
    :param ore: l'ora desiderata. Accetta input a 12 o 24 h
    :param minuti: i minuti desiderati
    :returns: l'angolo di apertura della lancetta rispetto alla posizione 0
    """
    grado_rotazione_ore = 360 // 12
    return ((ore * grado_rotazione_ore) % 360) + (angolo_minuti(minuti))//12


def crea_lancetta_secondi(angolo: int) -> Immagine:
    """
    Crea la lancetta dei secondi in posizione ore 0
    
    :param angolo: angolo di apertura della lancetta
    :returns: una lancetta ruotata
    """
    pallino_lancetta = cambia_punto_riferimento(
        cerchio(RAGGIO_PALLINO_ROSSO, ROSSO), 
        "middle", "middle")
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(LUNGHEZZA_LANCETTA_TESTA_SECONDI, ALTEZZA_LANCETTA_SECONDI, ROSSO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(LUNGHEZZA_LANCETTA_CODA_SECONDI, ALTEZZA_LANCETTA_SECONDI, ROSSO)),
        "left", "middle")
    lancetta_orizzontale = affianca(
        lancetta_testa, affianca(lancetta_coda, pallino_lancetta))
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    return ruota(lancetta_verticale, -(angolo))

controlla_valore_atteso(altezza_immagine(crea_lancetta_secondi(90)), RAGGIO_PALLINO_ROSSO * 2)


def angolo_secondi(secondi: int) -> int:
    """
    Definisce il grado di rotazione rispetto ai secondi
    
    :param secondi: la posizione della lancetta
    :returns: l'angolo di apertura della lancetta rispetto alla posizione 0
    """
    angolo = secondi * 6
    return angolo
