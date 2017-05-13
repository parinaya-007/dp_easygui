import easygui
import sys

def select_choice(name):
    msg = "Reading book \"" + name + "\". Choose the output formats"
    title = "Output Formats"
    choices = ["Text Generation", "Translation", "Audio Generation"]
    choice = easygui.multchoicebox(msg, title, choices)
    return choices, choice

def job_in_progress(choice):
    text = choice + " in progress..."
    easygui.textbox(text = text)

def job_done(choice):
    easygui.textbox(text = choice + " completed.")

def main():
    book_name = easygui.enterbox("Enter Book Name", "Book Name")

    if book_name == "":
        easygui.msgbox("No book name given.", "error")
        exit()

    given_choices, selected_choices = select_choice(book_name)
    if selected_choices:
        for choice in selected_choices:
            job_in_progress(choice)
            #Insert job function call here.
            job_done(choice)
    else:
        exit()

main()
