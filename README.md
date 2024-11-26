# White Background Generator for JPEG

White Background Generator for JPEG is a Python-based GUI application designed to process JPEG images by placing them on a white canvas with user-defined margins. The tool is intuitive and perfect for image preparation workflows that require consistent formatting and background management.

## Features
- **Customizable Margins**: Specify the margin size (default: 62 pixels) for precise image placement.
- **Simple GUI**: A clean, user-friendly interface built with Tkinter.
- **Image Resizing**: Automatically resizes images to fit a 1440x1440 canvas while maintaining aspect ratio.
- **Batch Processing**: Processes all JPEG images in a selected folder.
- **Output Management**: Saves processed images in a new `WB` folder within the selected directory.

---

## Installation

### Prerequisites
- Python 3.7 or newer
- Required Python libraries:
  - `Pillow` for image processing
  - `Tkinter` for GUI (comes pre-installed with Python)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone git@github.com:stevezzh819/White-Background-Generator-for-JPEG.git
   cd White-Background-Generator-for-JPEG
2. Run the application:
   ```bash
   python WB_app.py

## Usage

### Running the Application
1. Launch the application:
   ```bash
   python WB_app.py
2. Follow these steps:
   - **Select Folder**: Click "Browse" to choose a folder containing JPEG images.
   - **Set Margin**: Enter the margin size in pixels (default is 62).
   - **Process Images**: Click "Start Processing" to generate images with the specified settings.

3. The processed images will be saved in a new folder named `WB` inside the selected directory.

---

## Example Workflow
1. **Original Images**:
   - A folder contains several JPEG images with varying sizes.

2. **Processed Output**:
   - Each image is placed on a 1440x1440 white canvas.
   - Margins are added as specified.
   - Images are saved with the same filename in the `WB` folder.
---

## Development

### File Structure
```plaintext
White-Background-Generator-for-JPEG/
├── image_processor_gui.py  # Main application script
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── dist/                   # Packaged executable (if built)

## Contributing
Contributions are welcome! If you have ideas for improvements, feel free to fork the repository and submit a pull request.

---

## Contact
For questions or support, please contact:
- **Author**: Steve Zhang
- **Email**: zhangzehua819@gmail.com
- **GitHub**: [stevezzh819](https://github.com/stevezzh819)
