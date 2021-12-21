"""
Il file contiene funzioni che permettono la costruzione e l'animazione di un
orologio stile FFS che indica ore e minuti e secondi
In particolare le funzioni permettono di:
- creare un orologio stile FFS con indicazione su ore, minuti e secondi
- creare l'animazione dei secondi dell'orologio
"""
from img_lib_v0_6 import(
    Immagine, 
    componi, 
    crea_gif,
    larghezza_immagine,
    altezza_immagine,
)

from testing_util import(
    controlla_valore_atteso
)

from quadrante import(
    DIAMETRO_SFONDO,
    crea_quadrante
)

from lancette import(
    crea_lancetta_minuti,
    crea_lancetta_ore,
    crea_lancetta_secondi,
    angolo_secondi,
    angolo_minuti,
    angolo_ore
)


def crea_orologio(ore: int, minuti: int, secondi: int) -> Immagine:
    """
    Cra un orologio stile FFS con le lancette all'ora e al minuto desiderato
    
    :param ore: l'ora rispetto alla quale si deve posizionare la lancetta 
    delle ore. Accettati il formato 12h e 24h
    :param minuti: i minuti rispetto ai quali si deve posizionare la lancetta 
    dei minuti
    :param secondi: i secondi rispetto ai quali si deve posizionare la
    lancetta dei secondi
    :returns: un orologio stile FFS con l'ora, i minuti e secondi desiderati
    """
    ore_minuti = componi(crea_lancetta_ore(angolo_ore(ore, minuti)), 
                         crea_lancetta_minuti(angolo_minuti(minuti)))
    lancette = componi(crea_lancetta_secondi(angolo_secondi(secondi)),
                       ore_minuti)
    return componi(lancette, crea_quadrante())

controlla_valore_atteso(larghezza_immagine(crea_orologio(4, 10, 15)), DIAMETRO_SFONDO)
controlla_valore_atteso(altezza_immagine(crea_orologio(4, 10, 15)), DIAMETRO_SFONDO)


def crea_animazione_orologio(ore: int, minuti: int, secondi: int) -> Immagine:
    """
    Crea l'animazione di un orologio con la lancetta dei secondi che si muove 
    da 0 a secondi
    
    param ore: la posizione della lancetta delle ore
    param minuti: la posizione della lancetta dei minuti
    param minuti: la posizione della lancetta dei secondi
    returns: la gif animata di un orologio con i secondi che avanzano
    """
    lista_orologi = [
        crea_orologio(ore, minuti, passo)
        for passo in range(0, secondi)
    ]
    velocita = (40 * 1000 //40)
    return crea_gif("animazione_orologio",lista_orologi, velocita)

# crea_animazione_orologio(11, 15, 59)
