from tkinter import *
from tkinter import messagebox


def get_answer():

    question = user_input.get().lower()

    if question.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a question!"
        )
        return

    answer = "Sorry, I don't know the answer."

    if "ai" in question:
        answer = "AI stands for Artificial Intelligence. It enables machines to learn and make decisions."

    elif "python" in question and "develop" not in question:
        answer = "Python is a popular high-level programming language used for web development, AI, data science, and more."

    elif "develop" in question and "python" in question:
        answer = "Python was developed by Guido van Rossum in 1991."

    elif "machine learning" in question:
        answer = "Machine Learning is a subset of AI where computers learn from data."

    elif "codealpha" in question:
        answer = "CodeAlpha provides internships and project opportunities for students."

    elif "hello" in question or "hi" in question:
        answer = "Hello! How can I help you today?"

    answer_box.config(state=NORMAL)
    answer_box.delete("1.0", END)
    answer_box.insert(END, answer)
    answer_box.config(state=DISABLED)


# Main Window
root = Tk()

root.title("FAQ Chatbot")
root.geometry("750x550")
root.configure(bg="#E8DFF5")   # Pastel Purple


# Title
Label(
    root,
    text="🤖 FAQ Chatbot",
    font=("Comic Sans MS", 24, "bold"),
    bg="#E8DFF5",
    fg="#6A0DAD"
).pack(pady=20)


# Instructions
Label(
    root,
    text="Ask anything about AI, Python, Machine Learning or CodeAlpha",
    font=("Arial", 11),
    bg="#E8DFF5"
).pack()


# Input Box
user_input = Entry(
    root,
    width=50,
    font=("Arial", 14)
)

user_input.pack(pady=20)


# Button
Button(
    root,
    text="Get Answer",
    command=get_answer,
    bg="#FF69B4",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=10
).pack()


# Output Label
Label(
    root,
    text="Chatbot Response",
    font=("Arial", 12, "bold"),
    bg="#E8DFF5"
).pack(pady=15)


# Output Box
answer_box = Text(
    root,
    height=8,
    width=65,
    font=("Arial", 12),
    state=DISABLED,
    bg="#FFF5EE"
)

answer_box.pack()


root.mainloop()
