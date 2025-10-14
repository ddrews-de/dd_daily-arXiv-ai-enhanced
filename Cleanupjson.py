import json

def remove_duplicate_lines(input_file, output_file):
    """
    Read a jsonl file and remove duplicate lines
    
    Args:
        input_file (str): Path to the input jsonl file
        output_file (str): Path to the output jsonl file where deduplicated content will be saved
    """
    # Set to store unique lines
    unique_lines = set()
    
    # Read input file and write unique lines to output file
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Skip empty lines
            if not line.strip():
                continue
                
            # Only write line if we haven't seen it before
            if line not in unique_lines:
                unique_lines.add(line)
                outfile.write(line)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file.jsonl output_file.jsonl")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    remove_duplicate_lines(input_file, output_file)
    print(f"Duplicate lines removed. Result saved to {output_file}")
