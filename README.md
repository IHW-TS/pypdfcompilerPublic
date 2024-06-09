# PDFCompressor

PDFCompressor is a simple application for compressing multiple PDF files. The tool uses Ghostscript to perform file compression, allowing the reduction of PDF file sizes without significant quality loss. An improved version with an optimized user interface is planned for an upcoming update.

## Features

- Selection of multiple PDF files for compression.
- Choice of compression level: `screen`, `ebook`, `printer`, `prepress`, and `default`.
- Resetting the file selection.
- Saving compressed files with a name and location specified by the user.

## Usage

1. **Download and Execution:**
   - Download the compiled application from [the releases](https://github.com/IHW-TS/pypdfcompiler/releases).
   - Extract the content and execute `PDFCompressor.exe`.

2. **File Selection:**
   - Click on the "Select PDFs" button to choose the PDF files to compress.

3. **Compression Level Choice:**
   - Select the desired compression level from the dropdown menu.

4. **Compression and Saving:**
   - Click on "Compress" to compress the files.
   - Choose the saving location and the name for the compressed file.

5. **Resetting the Selection:**
   - Click on "Reset" to clear the file selection.

## Dependencies

The application uses Ghostscript for PDF compression. Ghostscript is included with the executable, so no additional installation is necessary.

## Compilation

If you want to compile the project yourself, follow the instructions below:

1. **Prerequisites:**
   - Install [Python](https://www.python.org/downloads/).
   - Install [PyInstaller](https://pyinstaller.org/).

```bash
pip install pyinstaller
  ```

2. **Project Download**

Clone the GitHub repository:

```bash
Copier le code
git clone https://github.com/your-username/PDFCompressor.git
cd PDFCompressor
```

3.Compilation:

Use PyInstaller to create the executable:

```bash
pyinstaller PDFCompressor.spec
```
The executable will be generated in the dist/PDFCompressor directory.

## Future Versions
I am currently working on version 2 of PDFCompressor with an enhanced and more intuitive user interface. Stay tuned for updates!

## Contributions
Contributions are welcome! If you have suggestions or improvements, feel free to create an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
