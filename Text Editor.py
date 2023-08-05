import tkinter as tk
from tkinter import filedialog


###########################################################################################################

def save_content():
#retrieves all the text content from the tk.Text widget starting from the first character
#(line 1, column 0) up to the last character (the end of the text).
    content = text_widget.get("1.0", tk.END)
#prompts a dialog box that asks the user to specify a name for the file and sets the file extension type
#as .txt.
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
#Checks if the file_path variable is a non-empty string.
    if file_path:
#If the if condition is true, these lines open the file path and write the actual data to be saved
        with open(file_path, "w") as file:
            file.write(content)




def load_content():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, content)

###########################################################################################################

#Settings for the window
root = tk.Tk()
root.title("Hold Nothing Back")
root.geometry("1000x800")


#Title
label = tk.Label(root, text="Super Secure Notepad for Venting About Government Secrets",
                 font=("Arial", 20), fg="black", anchor="center")
#Places the label widget into the window
label.place(x=125, y=40)

#Determines how text will behave when it reaches the right edge of the window,
#and size of the box by characters width, and lines height
text_widget = tk.Text(root, width=100, height=40, wrap="word")

#Places the widget (text box) into the window and I use place() instead of pack() for more control
text_widget.place(x=100, y=100)

#Creates a vertical scroll bar widget attached to text_widget (the command=text_widget attaches them)
#and the .yview says that the scrollbar changes the view of the text_widget in accordance with scrolling
vertical_scrollbar = tk.Scrollbar(root, command=text_widget.yview)
#Connects the text box with the scrollbar so that when you scroll, the text is moved accordingly
#"yscrollcommand" links the scrollbar to the text widget
#vertical_scrollbar.set tells the text box view to be adjusted by the scrollbar's position
text_widget.config(yscrollcommand=vertical_scrollbar.set)
#Places the scrollbar
vertical_scrollbar.pack(side="right", fill="y")

#Save Button
save_button = tk.Button(root, text="Save", command=save_content)
save_button.place(x=100, y=75)

#Load Button
load_button = tk.Button(root, text="Load", command=load_content)
load_button.place(x=140, y=75)

def on_closing():
    save_content()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

#Keeps the window running
root.mainloop()



###########################################################################################################
