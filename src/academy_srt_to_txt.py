import os

"""
    Converts SRT files from the folder srt_files to TXT files in the folder txt_files.
"""

# Set up the source and destination directories
src_folder = "../srt_files/"
dest_folder = "../txt_files/"

# Make sure the destination folder exists; if not, create it
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

# Loop through each file in the source folder
for filename in os.listdir(src_folder):
    if filename.endswith(".srt"):
        # Open the SRT file and read its contents
        with open(os.path.join(src_folder, filename), "r") as srt_file:
            srt_contents = srt_file.read()

        # Split the SRT file into individual subtitle entries
        subtitle_entries = srt_contents.strip().split("\n\n")

        # Extract the text from each subtitle entry and group into groups of three sentences
        text_entries = []
        for entry in subtitle_entries:
            lines = entry.split("\n")[2:]
            # Remove empty lines from the text
            lines = [line for line in lines if line.strip()]
            text = " ".join(lines).replace("\n", " ")
            text_entries.append(text)

        # Combine every three sentences and add a new line
        combined_text_entries = []
        for i in range(0, len(text_entries), 3):
            combined_text_entries.append(" ".join(text_entries[i:i+3]))

        # Combine all the text entries into a single string
        txt_contents = "\n".join(combined_text_entries)

        # Save the plain text to a new file in the destination folder
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        with open(os.path.join(dest_folder, txt_filename), "w") as txt_file:
            txt_file.write(txt_contents)

        print(f"Converted {filename} to {txt_filename}")
