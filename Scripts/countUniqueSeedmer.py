def count_unique_sequences(sequence_dict):
    unique_sequences = set()
    previous_seq = None
    
    for sequence, count in sequence_dict.items():
        # Check if the current sequence is unique based on the condition
        if previous_seq is None or previous_seq[1:-1] != sequence[:-1]:
            unique_sequences.add(sequence)
        
        # Update the last character of the current sequence
        previous_seq = sequence
    
    return len(unique_sequences)