import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import subprocess
import os

class PDFCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Compressor")
        self.selected_files = []
        self.create_widgets()

    def create_widgets(self):
        self.select_button = tk.Button(self.root, text="Select PDFs", command=self.select_files)
        self.select_button.pack(pady=10)

        self.file_list = tk.Listbox(self.root, width=60, height=10)
        self.file_list.pack(pady=10)

        self.compression_label = tk.Label(self.root, text="Select Compression Level:")
        self.compression_label.pack(pady=10)

        self.compression_var = tk.StringVar(value='screen')
        self.compression_options = ['screen', 'ebook', 'printer', 'prepress', 'default']
        self.compression_menu = tk.OptionMenu(self.root, self.compression_var, *self.compression_options)
        self.compression_menu.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_files)
        self.reset_button.pack(pady=10)

        self.compress_button = tk.Button(self.root, text="Compress", command=self.compress_files)
        self.compress_button.pack(pady=10)

    def select_files(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if files:
            self.selected_files = files
            self.update_file_list()

    def update_file_list(self):
        self.file_list.delete(0, tk.END)
        for file in self.selected_files:
            self.file_list.insert(tk.END, file)

    def reset_files(self):
        self.selected_files = []
        self.update_file_list()

    def compress_files(self):
        if not self.selected_files:
            messagebox.showwarning("Warning", "No files selected!")
            return

        # Select output directory and file name in one dialog
        output_file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save Compressed PDF as"
        )
        if not output_file_path:
            return

        compression_level = self.compression_var.get()

        gs_command = [
            'gswin64c', '-sDEVICE=pdfwrite', f'-dPDFSETTINGS=/{compression_level}', '-dNOPAUSE', '-dBATCH',
            '-sOutputFile=' + output_file_path
        ]
        gs_command.extend(self.selected_files)

        try:
            subprocess.run(gs_command, check=True)
            messagebox.showinfo("Success", f"Files compressed successfully to {output_file_path}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred during compression: {e}")




if __name__ == "__main__":
    root = tk.Tk()
    app = PDFCompressorApp(root)
    root.mainloop()