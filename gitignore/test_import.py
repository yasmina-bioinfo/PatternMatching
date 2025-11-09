import pattern_matching

# Appel direct d'une fonction depuis le module
seq = pattern_matching.read_sequence("data/tiny_genome.txt")
result = pattern_matching.positions_of("ATA", seq)
print(result)
