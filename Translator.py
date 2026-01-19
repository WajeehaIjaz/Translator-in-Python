from tkinter import *          # Import components (*, Button, Label, Text, etc.)
from tkinter import ttk        # for modern themed widgets like Combobox
from deep_translator import GoogleTranslator

#source->dest lang
def change(text="type", src="en", dest="ur"):
    translator = GoogleTranslator(source=src, target=dest)     #translator object
    result = translator.translate(text)
    return result

def data():
    s = comb_sor.get()           # Get the selected source language from source combobox
    d = comb_dest.get()          # Get the selected destination language from destination combobox

    # Get all text from source text box (1.0 = line 1, character 0)
    # END = until the end, strip() removes extra whitespace
    msg = sor_txt.get(1.0, END).strip()
    
    # Dictionary mapping language names to their language codes
    # 'english' maps to 'en', 'urdu' maps to 'ur', etc.
    lang_codes = {
        'english': 'en',
        'urdu': 'ur',
        'spanish': 'es',
        'french': 'fr',
        'german': 'de',
        'chinese (simplified)': 'zh-CN',
        'arabic': 'ar',
        'hindi': 'hi',
        'japanese': 'ja',
        'russian': 'ru'
    }
    
    # Try-except block to handle any errors during translation
    try:
        # Convert language name to code (lowercase for matching)
        # If language not found, default to 'en' (English)
        src_code = lang_codes.get(s.lower(), 'en')
        # Convert destination language name to code
        # If language not found, default to 'en' (English)
        dest_code = lang_codes.get(d.lower(), 'en')
        
        textget = change(text=msg, src=src_code, dest=dest_code)
        # Clear the destination text box (delete all content) for next
        dest_txt.delete(1.0, END)
        # Insert the translated text into destination text box
        dest_txt.insert(END, textget)
    # If any error occurs during translation
    except Exception as e:
        # Clear the destination text box
        dest_txt.delete(1.0, END)
        # Display the error message to the user
        dest_txt.insert(END, f"Error: {str(e)}")

root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg="grey")

# Create a label for the main heading "Translator"
lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"))
lab_txt.place(x=100, y=30, height=50, width=300)

# Create a label for "Source Text" heading
lab_txt2 = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), bg="grey", fg="black")
lab_txt2.place(x=100, y=100, height=20, width=300)

# Create a multi-line text box for entering source text
sor_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
sor_txt.place(x=10, y=130, height=150, width=480)

# Create a list of popular languages to show in dropdown menus
lang_list = ['English', 'Urdu', 'Spanish', 'French', 'German', 'Chinese (simplified)', 'Arabic', 'Hindi', 'Japanese', 'Russian']

# Create a dropdown (Combobox) for selecting source language
comb_sor = ttk.Combobox(root, values=lang_list)
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("English")             # Set default value to "English"


# Create the "Translate" button that triggers the translation
# command=data means it calls the data() function when clicked
button_change = Button(root, text="Translate", relief=RAISED, command=data)
button_change.place(x=175, y=300, height=40, width=150)

# Create a dropdown (Combobox) for selecting destination language
comb_dest = ttk.Combobox(root, values=lang_list)
comb_dest.place(x=340, y=300, height=40, width=150)
# Set default value to "English"
comb_dest.set("English")

# Create a label for "Dest Text" (Destination Text) heading
lab_txt3 = Label(root, text="Dest Text", font=("Times New Roman", 20, "bold"), bg="grey", fg="black")
lab_txt3.place(x=100, y=360, height=20, width=300)

# Create a multi-line text box for displaying translated text
dest_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()