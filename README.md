# PDF Text-to-Speech Reader

This Python application allows you to extract text from a PDF and convert it to speech using the `pyttsx3` library. You can select specific pages to read, configure the voice settings, and even save the spoken audio as an MP3 file.

---

## Features

1. **PDF Text Extraction**  
   Extracts text from the selected pages of a PDF file.

2. **Text-to-Speech Conversion**  
   Uses `pyttsx3` to convert the extracted text into speech with customizable voice options.

3. **Audio File Saving**  
   Saves the spoken text as an MP3 file.

4. **Metadata Viewer**  
   Displays the PDF's metadata and the number of pages.

---

## Requirements

- Python 3.x
- Libraries:  
  - `PyPDF2` (for PDF parsing)  
  - `pyttsx3` (for text-to-speech)  

Install the required libraries using:
*add requiurements text later
```bash
pip install PyPDF2 pyttsx3
```

---

## How to Use

1. **Run the Script**  
   Execute the script in your terminal:

   ```bash
   python Shitty tts.py
   ```

2. **Enter File Path**  
   Provide the file path to the PDF you want to process.

3. **Select a Page**  
   Enter the page number you want to extract text from. Enter `00` to exit the program.

4. **Choose Voice Settings**  
   - Select a voice ID.(They suck)
   - Customize the speech rate and volume.

5. **Save Audio**  
   Specify a file name with the `.mp3` extension to save the speech output.

6. **View Metadata**  
   The script also displays the PDF's metadata, such as the title and the total number of pages.

---


## Example Usage

```text
Enter File Path: path to pdf file
The selected pdf: Sample Document
Number of pages: 10 pages
Enter the page number you want to check for: 3
0:Microsoft Zira Desktop
1:Microsoft David Desktop
The voice ID you want to use: 0
Enter the option you want to use:
1: rate
2: Volume
Enter rate: 150
What do you want to name the saved file (must end in an mp3 ext): output.mp3
File has been saved.
voice playback starts
```

---
