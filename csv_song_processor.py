import csv

def get_unique_songs(input_filename):
    """
    The function `get_unique_songs` reads a CSV file and returns a set of unique songs, where each song
    is represented as a string in the format "song name by artist".
    
    :param input_filename: The input_filename parameter is the name of the CSV file that contains the
    songs data
    :return: a set of unique songs.
    """
    unique_songs = set()

    with open(input_filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            song = f"{row[2]} by {row[3]}"
            unique_songs.add(song)

    return unique_songs

def write_unique_songs_to_file(output_filename, unique_songs):
    """
    The function writes a list of unique songs to a file, with each song on a new line.
    
    :param output_filename: The name of the file where the unique songs will be written to
    :param unique_songs: The `unique_songs` parameter is a list of strings, where each string represents
    a unique song
    """
    with open(output_filename, "w") as file:
        file.writelines(line + "\n" for line in unique_songs)

if __name__ == "__main__":
    input_file = input("Enter the CSV filename: ")
    output_file = input("Enter the output filename: ")

    unique_songs = get_unique_songs(input_file)
    write_unique_songs_to_file(output_file, unique_songs)

    print(f"Processing complete. Unique songs written to {output_file}")