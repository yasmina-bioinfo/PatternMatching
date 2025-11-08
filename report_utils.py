import csv, os

def summarize_to_console(results):
    """Affiche un résumé clair dans le terminal."""
    print("\n===== RÉCAPITULATIF =====")
    print("Motif\tNb_occurrences\tPositions")
    for motif, positions in results:
        print(f"{motif}\t{len(positions)}\t{positions}")

def save_csv(results, filename="results.csv", folder="data"):
    """Enregistre les résultats dans un fichier CSV."""
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Motif", "Nb_occurrences", "Positions"])
        for motif, positions in results:
            writer.writerow([motif, len(positions), " ".join(map(str, positions))])
    print(f"\n✅ CSV enregistré ➜ {path}")
