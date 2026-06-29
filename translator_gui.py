from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator


def translate_text():
    try:
        text = input_box.get("1.0", END).strip()

        if text == "":
            messagebox.showwarning("Warning", "Please enter some text!")
            return

        translated = GoogleTranslator(
            source=languages[source_lang.get()],
            target=languages[target_lang.get()]
        ).translate(text)

        output_box.delete("1.0", END)
        output_box.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Main Window
root = Tk()
root.title("Language Translation Tool")
root.geometry("700x500")
root.configure(bg="#FFDDEE")   # Pastel pink background


# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja"
}


# Title
Label(
    root,
    text="🌍 Language Translation Tool",
    font=("Arial", 20, "bold"),
    bg="#FFDDEE",
    fg="#7B2CBF"
).pack(pady=10)


# Dropdown Frame
frame = Frame(root, bg="#FFDDEE")
frame.pack()

source_lang = StringVar(value="English")
target_lang = StringVar(value="Hindi")

ttk.Combobox(
    frame,
    textvariable=source_lang,
    values=list(languages.keys()),
    width=20
).grid(row=0, column=0, padx=20)

ttk.Combobox(
    frame,
    textvariable=target_lang,
    values=list(languages.keys()),
    width=20
).grid(row=0, column=1, padx=20)


# Input Box
Label(
    root,
    text="Enter Text",
    bg="#FFDDEE",
    font=("Arial", 12)
).pack(pady=5)

input_box = Text(
    root,
    height=6,
    width=60
)

input_box.pack()


# Translate Button
Button(
    root,
    text="Translate",
    command=translate_text,
    bg="#FF69B4",
    fg="white",
    font=("Arial", 12, "bold")
).pack(pady=15)


# Output Box
Label(
    root,
    text="Translated Text",
    bg="#FFDDEE",
    font=("Arial", 12)
).pack()

output_box = Text(
    root,
    height=6,
    width=60
)

output_box.pack()


root.mainloop()
