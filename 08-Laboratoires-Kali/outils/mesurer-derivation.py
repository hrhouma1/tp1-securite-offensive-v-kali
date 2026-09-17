"""Mesure pédagogique relative, sans benchmark matériel universel."""
import hashlib
import time

mot = b"mot-de-passe-fictif"
sel = b"sel-fictif-boreal"
def mesurer(fonction, repetitions):
    debut = time.perf_counter()
    for _ in range(repetitions):
        fonction()
    return (time.perf_counter() - debut) / repetitions

rapide = mesurer(lambda: hashlib.sha256(mot).digest(), 10000)
derive = mesurer(lambda: hashlib.pbkdf2_hmac("sha256", mot, sel, 100000), 5)
print(f"SHA-256 : {rapide:.9f} seconde par calcul")
print(f"PBKDF2 à 100000 itérations : {derive:.6f} seconde par calcul")
print(f"Rapport observé sur cette machine : {derive / rapide:.1f}")
print("100000 est un paramètre d'expérience, pas une recommandation de production.")
