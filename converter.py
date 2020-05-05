from tkinter import *
from custom_dict import *

root = Tk()
root.title("Text Converter")
# root.iconbitmap("A51_0000.ico")
root.resizable(False, False)
# Frame to hold window contents
frame = LabelFrame(root, padx=15, pady=15)
frame.grid(padx=10, pady=10)

# Create clipboard and hide window
clip = Tk()
clip.withdraw()


# Create radio buttons
option = IntVar()
Radiobutton(frame, text="Roman Numeral", variable=option, value=1).grid(row=2, column=0, sticky=W)
Radiobutton(frame, text="NATO Phonetic", variable=option, value=2).grid(row=3, column=0, sticky=W)
option.set(1)


##########################################################
######                  FUNCTIONS                   ######
##########################################################
# Convert and fill output field (functions for button-click or Enter)
def convert_enter(event):
    global dictionary_roman
    global dictionary_NATO
    global option
    # Clear previous output, if any
    entry_output.delete(0, END)
    # Convert string to char array
    list_entry = list(entry_input.get())

    if option.get() == 1:
        for index,item in enumerate(list_entry):
            for key,value in dictionary_roman.items():
                if item==key:
                    list_entry[index] = value
    else:
        for index,item in enumerate(list_entry):
            for key,value in dictionary_NATO.items():
                if item==key:
                    list_entry[index] = value
    
    result = (" ".join(list_entry))

    entry_output.insert(0, result)

def convert(event=None):
    global dictionary_roman
    global dictionary_NATO
    global option
    # Clear previous output, if any
    entry_output.delete(0, END)
    # Convert string to char array
    list_entry = list(entry_input.get())

    if option.get() == 1:
        for index,item in enumerate(list_entry):
            for key,value in dictionary_roman.items():
                if item==key:
                    list_entry[index] = value
    else:
        for index,item in enumerate(list_entry):
            for key,value in dictionary_NATO.items():
                if item==key:
                    list_entry[index] = value
    
    result = (" ".join(list_entry))

    entry_output.insert(0, result)

# Bind convert function to Enter/Return key
root.bind("<Return>", convert)


# Clipboard function
def clipboard():
    clip.clipboard_clear()
    clip.clipboard_append(entry_output.get())
    clip.update()

# Quit function for clean process quit
def quit():
    root.quit
    root.destroy()
    sys.exit()

# Kill process on window close
root.protocol("WM_DELETE_WINDOW", quit)


##########################################################
######                 FORM FIELDS                  ######
##########################################################
# Input label
label_input = Label(frame, text="Text:")
label_input.grid(row=0, column=0)
# Input field
entry_input = Entry(frame, width=75, borderwidth=3)
entry_input.grid(row=0, column=1, padx=5, pady=5)

# Output label
label_input = Label(frame, text="Conversion:")
label_input.grid(row=1, column=0)
# Output field
entry_output = Entry(frame, width=75, borderwidth=3)
entry_output.grid(row=1, column=1, padx=5, pady=5)


##########################################################
######                   BUTTONS                    ######
##########################################################
# Submit
button_convert = Button(frame, text="Convert", command=convert)
button_convert.grid(row=2, column=1, padx=5, pady=5, sticky=E+W)

# Copy to clipboard
button_clipboard = Button(frame, text="Copy to Clipboard", command=clipboard)
button_clipboard.grid(row=3, column=1, padx=5, pady=5, sticky=E+W)


root.mainloop()