import easygui
import sys

def select_choice(name):
    msg = "Reading book \"" + name + "\". Choose any number of output formats : "
    title = "Output Formats"
    choices = ["Audio", "Text", "Text and Audio"]
    choice = easygui.multchoicebox(msg, title, choices)
    return choices, choice

def job_in_progress(selected_choices):
    text = ''
    for choice in selected_choices:
        text = text + choice + " process, "
    text = text + "are in progress....."
    easygui.textbox(text = text)

def job_done():
    easygui.textbox(text = "Processes completed.")

def main():
    book_name = easygui.enterbox("Enter Book Name : ", "Book Name")
    given_choices, selected_choices = select_choice(book_name)
    if selected_choices:
        job_in_progress(selected_choices)
        job_done()
    else:
        exit()

main()
