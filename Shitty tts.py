import sys
import pyttsx3
from PyPDF2 import PdfReader


class Reader:
    def __init__(self):
        self.storage = []  # store the extracted text from the pdf
        self.engine = pyttsx3.init()

    def set_reader(self, path):
        try:
            with open(path, 'rb') as file:
                pdf = PdfReader(file)
                max_page = len(pdf.pages)
                print(f'The selected pdf:{pdf.metadata.title}\nNumber of pages:{max_page} pages')
                while True:
                    select_page = int(input("enter the page number you want to check for: "))
                    if select_page == 00:
                        print("program has been terminated")
                        sys.exit(0)
                    if select_page > max_page:
                        print("sorry you are outside the page limit")

                    # extract text and stor in the storage list
                    pages = pdf.pages[select_page]
                    extracted_text = pages.extract_text()
                    self.storage.append(extracted_text)

                    self.read_text()
                    # remove contents after first read
                    # to prevent it from reading it again if another page is selected
                    self.storage.clear()
        except FileNotFoundError as e:
            print(f"Sorry can't find that {e}")
        except IndexError as e:
            print(f'{e}')

    def read_text(self):
        # convert the stored text in the storage list  to a string
        text = "".join(self.storage)

        voices = self.engine.getProperty('voices')
        # list all current voices
        # note the default voices do suck ass so yh heads up
        for i, voice in enumerate(voices):
            print(f'{i}:{voice.name}')

        voice_id = int(input("the voice id you want to use: "))
        self.option()
        self.engine.setProperty('voice', voices[voice_id].id)
        self.engine.say(text)

        # save or some shit
        file_name = input("What do you want to name the saved file(must end in a mp3 ext): ")
        if not file_name.endswith(".mp3"):
            print("invalid file extension used")
        else:
            self.engine.save_to_file(text, file_name)
            print("file has been saved")
            self.engine.runAndWait()

    @staticmethod
    def get_info(path):
        try:
            # display various metadata of the pdf
            with open(path, 'rb') as file:
                pdf = PdfReader(file)
                meta = pdf.metadata
                page_num = len(pdf.pages)

                text = (f"Tittle:{meta.title},"
                        f"Page_Num:{page_num}")
                print(text)
        except FileNotFoundError:
            print("error finding file")
        except IndexError:
            print("you over shot the index bro")

    def option(self):
        # create voice options,i.e speech rate,volume
        options = {"1": "rate",
                   "2": "Volume"}
        for key, value in options.items():
            print(f'{key}:{value}')

        options_select: str = input("enter the option you want to use: ")
        if options_select in options:
            opt = options[options_select]

            if opt == "rate":
                rate_value: int = int(input("Enter rate: "))
                if rate_value > 300:
                    print("sorry you definitely don't want to try this speed ")
                    sys.exit(1)
                else:
                    self.engine.setProperty('rate', rate_value)

            elif opt == "Volume":
                vol_value: float = float(input("Enter volume from(0.0 - 1.0): "))
                if vol_value > 1.0:
                    print("1.0 is the max please try again")
                    sys.exit(1)
                else:
                    self.engine.setProperty('volume', vol_value)
            else:
                print("invalid option")
                sys.exit(1)


if __name__ == "__main__":
    # create an instance
    me = Reader()
    # input file path to pdf
    path: str = input("Enter File Path: ")
    me.set_reader(path)
