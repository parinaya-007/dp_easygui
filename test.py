import easygui
import sys

def select_choice(name):
    msg = "Reading book \"" + name + "\". Choose the output formats"
    title = "Output Formats"
    choices = ["Text", "Translation", "Audio"]
    choice = easygui.multchoicebox(msg, title, choices)
    return choices, choice

def job_in_progress(selected_choices):
    text = ''
    for choice in selected_choices:
        text = text + choice + ", "
    text = text + " conversion process(es) "
    text = text + "in progress....."
    easygui.textbox(text = text)

def job_done():
    easygui.textbox(text = "Process(es) completed.")

def main():
    book_name = easygui.enterbox("Enter Book Name", "Book Name")
    given_choices, selected_choices = select_choice(book_name)
    if selected_choices:
        job_in_progress(selected_choices)
        job_done()
    else:
        exit()

main()
