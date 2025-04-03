import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import ipywidgets as widgets
from IPython.display import display
import os
import io



def upload_txt_file_2():
    """
    Creates a button that, when clicked, opens a file dialog to upload a .txt file
    to the current working directory.
    """

    def upload_file():
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filepath:
            try:
                filename = os.path.basename(filepath)
                with open(filepath, 'rb') as source, open(filename, 'wb') as destination:
                    destination.write(source.read())

                messagebox.showinfo("Upload Successful", f"File '{filename}' uploaded successfully.")
            except Exception as e:
                messagebox.showerror("Upload Error", f"An error occurred: {e}")

    root = tk.Tk()
    root.title("Upload .txt File")

    upload_button = tk.Button(root, text="Upload File", command=upload_file)
    upload_button.pack(padx=20, pady=20)

    root.mainloop()


def upload_txt_file3():
    filepath = input("Enter the path to the .txt file: ")
    if os.path.exists(filepath) and filepath.lower().endswith('.txt'):
        try:
            filename = os.path.basename(filepath)
            with open(filepath, 'rb') as source, open(filename, 'wb') as destination:
                destination.write(source.read())
            print(f"File '{filename}' uploaded successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid file path or file type.")




def upload_txt_file():
    """
    Creates a file upload button in the Jupyter cell output that allows the user
    to upload a .txt file to the current working directory.
    """

    def handle_upload(change):
        uploaded_file = change['new'][0]
        filename = uploaded_file['name']
        content = uploaded_file['content']
        try:
            with open(filename, 'wb') as f:
                f.write(content)
            print(f"File '{filename}' uploaded successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    uploader = widgets.FileUpload(
        accept='.txt',  # Accept only .txt files
        multiple=False  # Allow only single file upload
    )

    uploader.observe(handle_upload, names=['value'])
    display(uploader)

# Example usage (within a Jupyter Notebook cell):
# upload_txt_file()
# if __name__ == "__main__":
#     upload_txt_file()


# if __name__ == "__main__":
#     upload_txt_file()