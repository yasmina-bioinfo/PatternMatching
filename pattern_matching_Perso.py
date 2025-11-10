from report_utils import summarize_to_console, save_csv 
# These functions are imported to summarize the results and display them in a table

def positions_of(motif, DNA):
    # looking for all the positions of a pattern
    p = len(motif) # p represents the pattern we're looking for.
    d = len(DNA) # d represents the DNA sequence.
    positions = [] # list to save all the positions found.
    for i in range (d - p + 1): # for all p positions in the DNA sequence.
        window = DNA[i:i+p] # We scan through the sequence to retrieve all positions where the target pattern occurs.
        if window == motif: # For each segment of the sequence, check if it matches the target pattern.
            positions.append(i) #For each segment of the sequence, check if it matches the target pattern.
    return positions 

def read_fasta(filepath): # Read the DNA sequence from the FASTA file or a text.
    sequence = [] #Create an empty list to store the sequence fragments read from the file.
    with open(filepath, 'r', encoding="utf-8") as f: # Open the file in read mode and automatically close it when finished.
        for line in f: #Iterate through each line of the file.
            line = line.strip() # Remove leading and trailing spaces or newline characters.
            if not line or line.startswith(">"): #Skip empty lines and header lines (FASTA format).
                continue 
            sequence.append(line) #Append the cleaned line to the sequence list.
    return "".join(sequence).upper() #Join all lines together and return the sequence in uppercase.

# --- Main program entry point ---
def main(): 
    DNA = read_fasta("data/tiny_genome.txt") #File reading
    motifs = ["CGA", "TTC", "TTT", "ATA"] #List of motifs to search for.
    results = [] # To store the results (motif and positions).

# Search each motif in the sequence.
    for motif in motifs:
        pos = positions_of(motif, DNA)
        results.append((motif, pos))
    if pos:
        print(f"OK '{motif}' trouvé {len(pos)} fois → {pos}")
    else: 
        print(f"NO '{motif}' non trouvé")

# Results on screen and save as CSV
    summarize_to_console(results)
    save_csv(results,"results_pattern_matching.csv")

#--- Automatic execution trigger ---
if __name__ == "__main__":
    main()