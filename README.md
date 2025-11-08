![Status](https://img.shields.io/badge/Status-Completed-success)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Field](https://img.shields.io/badge/Field-Bioinformatics-green)
![Type](https://img.shields.io/badge/Mini--Project-PatternMatching-lightgrey)

# Pattern Matching — Mini-Project 1
**Bioinformatics Algorithms in Practice**  
*(English / Français)*

---

## ENG Overview  
This mini-project implements a simple **pattern-matching algorithm** to locate all occurrences of a DNA motif within a genome sequence.  
It is part of a personal learning roadmap toward bioinformatics and genomic data science.

### Objective  
To understand how biological motif searches (such as promoter or restriction site detection) can be implemented from scratch in Python.

### Key Concepts  
- String traversal and substring comparison   
- Introduction to searching motifs (motif discovery)

### Example  
```python
pattern = "ATG"
genome  = "AATGCTATGCAATGC"
positions = pattern_matching(pattern, genome)
print(positions)
```

**Expected Output**  
```
Pattern 'ATG' found at positions: 1, 6, 11
```

### Files  
- `pattern_matching.py` → core algorithm  
- `results.csv` (optional) → exported results  
- `README.md` → documentation  

---

## 🇫🇷 Résumé  
Ce mini-projet met en œuvre un **algorithme de recherche de motif ADN** permettant d’identifier toutes les occurrences d’un motif donné dans une séquence génomique.  
Il s’inscrit dans ma feuille de route d’apprentissage vers la bio-informatique et la science des données génomiques.

### Objectif  
Comprendre comment les outils bio-informatiques recherchent des motifs biologiques (promoteurs, sites de restriction, etc.) à l’aide de comparaisons de chaînes de caractères en Python.

### Notions essentielles  
- Parcours d’une séquence par indices  
- Comparaison de sous-chaînes  
- Introduction à la recherche de motifs (motif discovery)

### Exemple  
```python
pattern = "ATG"
genome  = "AATGCTATGCAATGC"
positions = pattern_matching(pattern, genome)
print(positions)
```

**Résultat attendu**  
```
Motif 'ATG' trouvé aux positions : 1, 6, 11
```

### Fichiers  
- `pattern_matching.py` : code principal  
- `results.csv` : export éventuel des résultats  
- `README.md` : ce fichier explicatif  

--- 
> — Yasmina Soumahoro
