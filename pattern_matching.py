# --- Importations ---
from report_utils import summarize_to_console, save_csv

# --- Fonctions principales ---

def positions_of(pattern, text):
    """Renvoie la liste des positions où le motif apparaît dans le texte."""
    m = len(pattern)
    n = len(text)
    positions = []
    for i in range(n - m + 1):
        window = text[i:i+m]
        if window == pattern:
            positions.append(i)
    return positions


def read_sequence(path):
    """Lit une séquence ADN à partir d'un fichier texte ou FASTA."""
    seq = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(">"):
                continue
            seq.append(line)
    return "".join(seq).upper()


# --- Programme principal ---
def main():
    # Lecture du fichier
    text = read_sequence("data/tiny_genome.txt")

    # Liste des motifs à rechercher (tu peux en ajouter librement)
    motifs = ["GCG", "ATA", "TTT"]

    results = []  # pour stocker les résultats (motif, positions)

    # Recherche de chaque motif
    for motif in motifs:
        pos = positions_of(motif, text)
        results.append((motif, pos))
        if pos:
            print(f"✅ '{motif}' trouvé {len(pos)} fois → {pos}")
        else:
            print(f"⚠️ '{motif}' non trouvé")

    # Résumé à l’écran + sauvegarde CSV
    summarize_to_console(results)
    save_csv(results, "results_pattern_matching.csv")


# --- Lancement automatique ---
if __name__ == "__main__":
    main()
