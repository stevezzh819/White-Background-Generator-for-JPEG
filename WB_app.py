import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from PIL import Image
import threading

def process_images(folder_path, margin):
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder!")
        return

    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "Selected folder does not exist!")
        return

    jpeg_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg')]
    
    if not jpeg_files:
        messagebox.showinfo("No Files", "No JPEG files found in the selected folder.")
        return

    output_folder = os.path.join(folder_path, "WB")
    os.makedirs(output_folder, exist_ok=True)
    
    canvas_size = (1440, 1440)
    ppi = 300

    for idx, file in enumerate(jpeg_files, start=1):
        file_path = os.path.join(folder_path, file)
        try:
            img = Image.open(file_path)
        except FileNotFoundError:
            continue

        aspect_ratio = img.width / img.height
        
        if aspect_ratio >= 1:
            max_width = canvas_size[0] - 2 * margin
            new_width = max_width
            new_height = int(new_width / aspect_ratio)
        else:
            max_height = canvas_size[1] - 2 * margin
            new_height = max_height
            new_width = int(new_height * aspect_ratio)

        img_resized = img.resize((new_width, new_height), Image.LANCZOS)
        canvas = Image.new("RGB", canvas_size, "white")

        if aspect_ratio >= 1:
            x_offset = margin
            y_offset = (canvas_size[1] - new_height) // 2
        else:
            x_offset = (canvas_size[0] - new_width) // 2
            y_offset = margin

        canvas.paste(img_resized, (x_offset, y_offset))
        output_path = os.path.join(output_folder, f"{idx}.jpeg")
        canvas.save(output_path, "JPEG", dpi=(ppi, ppi))

    messagebox.showinfo("Success", "Processing completed. Images saved in <<WB>> folder.")

def browse_folder():
    def select_folder():
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            folder_entry.delete(0, "end")
            folder_entry.insert(0, folder_selected)
        app.focus_force()

    threading.Thread(target=select_folder, daemon=True).start()

def start_processing():
    process_button.config(state="disabled")  # Disable button during processing
    try:
        margin = int(margin_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid margin value!")
        process_button.config(state="normal")
        return

    if margin < 0:
        messagebox.showerror("Error", "Margin value cannot be negative!")
        process_button.config(state="normal")
        return

    def process():
        process_images(folder_entry.get(), margin)
        process_button.config(state="normal")  # Re-enable button after processing

    threading.Thread(target=process, daemon=True).start()

app = Tk()
app.title("White Background Processor")
app.geometry("700x300")
app.eval('tk::PlaceWindow . center')  # Center the window on the screen

Label(app, text="Select a folder with JPEG images:", font=("Helvetica", 14), pady=10).pack()

folder_entry = Entry(app, width=50, font=("Helvetica", 12))
folder_entry.pack(pady=5)

browse_button = Button(app, text="Browse", command=browse_folder, font=("Helvetica", 12), padx=10, pady=5, bg="#E0E0E0")
browse_button.pack(pady=5)

Label(app, text="Enter margin (pixels):", font=("Helvetica", 14), pady=10).pack()

margin_entry = Entry(app, width=10, font=("Helvetica", 12))
margin_entry.insert(0, "62")  # Default value of 62 pixels
margin_entry.pack(pady=5)

process_button = Button(app, text="Start Processing", command=start_processing, font=("Helvetica", 12), padx=20, pady=10, bg="#007AFF", fg="black")
process_button.pack(pady=20)

app.mainloop()
