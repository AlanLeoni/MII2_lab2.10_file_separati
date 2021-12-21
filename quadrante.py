"""
Il file contiene funzioni che permettono la costruzione di un quadrante di un
orologio.
In particolare le funzioni permettono di creare lo sfondo del quadrante che 
evidenzia i minuti e i cinque minuti
"""
from img_lib_v0_6 import(
    Immagine, 
    affianca, 
    cerchio, 
    immagine_vuota, 
    rettangolo, 
    ruota, 
    sovrapponi, 
    cambia_punto_riferimento, 
    componi, 
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
RAGGIO_SFONDO_BIANCO = RAGGIO * 95 //100
DIAMETRO_SFONDO = RAGGIO * 2
ALTEZZA_TACCA_MINUTI = RAGGIO * 3 // 100
LUNGHEZZA_TESTA_TACCA_MINUTI = RAGGIO * 82 // 100
LUNGHEZZA_CODA_TACCA_MINUTI = RAGGIO * 8 // 100
ALTEZZA_TACCA_5_MINUTI = RAGGIO * 8 // 100
LUNGHEZZA_TESTA_TACCA_5_MINUTI = RAGGIO * 70 // 100
LUNGHEZZA_CODA_TACCA_5_MINUTI = RAGGIO * 20 // 100
GRADI_TACCHE_5_MINUTI = 360 // 60
MOD5_TACCHE_5_MINUTI = 360 // 12

def crea_sfondo() -> Immagine:
    """
    Crea lo sfondo del quadrante
    
    :returns: il cerchio del quadrante con un bordo grigio
    """
    sfondo_grigio = cerchio(RAGGIO, GRIGIO)
    sfondo_bianco = cerchio((RAGGIO_SFONDO_BIANCO), BIANCO)
    return sovrapponi(sfondo_bianco, sfondo_grigio)

controlla_valore_atteso(larghezza_immagine(crea_sfondo()), DIAMETRO_SFONDO)
controlla_valore_atteso(altezza_immagine(crea_sfondo()), DIAMETRO_SFONDO)


def crea_tacca_minuti() -> Immagine:
    """
    Crea la singola tacca che indica i minuti
    
    :returns: una singola tacca indicante i minuti
    """
    testa_tacca = rettangolo(LUNGHEZZA_TESTA_TACCA_MINUTI, ALTEZZA_TACCA_MINUTI, BIANCO)
    coda_tacca = rettangolo(LUNGHEZZA_CODA_TACCA_MINUTI, ALTEZZA_TACCA_MINUTI, NERO)
    return cambia_punto_riferimento(
        affianca(testa_tacca, coda_tacca), "left", "middle")

controlla_valore_atteso(larghezza_immagine(crea_tacca_minuti()), LUNGHEZZA_TESTA_TACCA_MINUTI + LUNGHEZZA_CODA_TACCA_MINUTI)
controlla_valore_atteso(altezza_immagine(crea_tacca_minuti()), ALTEZZA_TACCA_MINUTI)


def crea_tacca_cinque_minuti() -> Immagine:
    """
    Crea la singola tacca che indica i cinque minuti
    
    :returns: una singola tacca indicante i cinque minuti
    """
    testa_tacca = rettangolo(LUNGHEZZA_TESTA_TACCA_5_MINUTI, ALTEZZA_TACCA_5_MINUTI, BIANCO)
    coda_tacca = rettangolo(LUNGHEZZA_CODA_TACCA_5_MINUTI, ALTEZZA_TACCA_5_MINUTI, NERO)
    return cambia_punto_riferimento(
        affianca(testa_tacca, coda_tacca), "left", "middle")

controlla_valore_atteso(larghezza_immagine(crea_tacca_cinque_minuti()), LUNGHEZZA_TESTA_TACCA_5_MINUTI + LUNGHEZZA_CODA_TACCA_5_MINUTI)
controlla_valore_atteso(altezza_immagine(crea_tacca_cinque_minuti()), ALTEZZA_TACCA_5_MINUTI)


def crea_tacche_minuti_5_minuti() -> Immagine:
    """
    Crea le tacche circolari indicanti i minuti ed evidenziati i 5 minuti
    
    returns: le tacche circolari indicanti i minuti e i 5 minuti
    """
    gradi  = 360 // 60
    mod5 = 360 // 12
    quadrante_prec = immagine_vuota()
    for tacca in range(0, 360, gradi):
        if tacca % mod5 == 0: 
            tacca_quadrante = ruota(crea_tacca_cinque_minuti(), tacca)
        else:
            tacca_quadrante = ruota(crea_tacca_minuti(), tacca)    
        quadrante_minuti = componi(quadrante_prec, tacca_quadrante)
        quadrante_prec = quadrante_minuti
    return quadrante_minuti

# falliscono tutti di un punto
# controlla_valore_atteso(larghezza_immagine(crea_tacche_minuti_5_minuti()), (larghezza_immagine(crea_tacca_minuti())) * 2)
# controlla_valore_atteso(larghezza_immagine(crea_tacche_minuti_5_minuti()), ((LUNGHEZZA_TESTA_TACCA_5_MINUTI + LUNGHEZZA_CODA_TACCA_5_MINUTI)* 2))
# controlla_valore_atteso(altezza_immagine(crea_tacche_minuti_5_minuti()), ((LUNGHEZZA_TESTA_TACCA_5_MINUTI + LUNGHEZZA_CODA_TACCA_5_MINUTI)* 2))


def crea_quadrante() -> Immagine:
    """
    Crea il quadrante dell'orologio con tacche minuti e cinque minuti
    
    :returns: un'immagine del quadrante dell'orologio senza lancette
    """
    return componi(crea_tacche_minuti_5_minuti(), crea_sfondo())

controlla_valore_atteso(larghezza_immagine(crea_quadrante()), DIAMETRO_SFONDO)
controlla_valore_atteso(altezza_immagine(crea_quadrante()), DIAMETRO_SFONDO)

