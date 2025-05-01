
# 🎹 Virtual Air Keyboard

A fun and interactive virtual piano keyboard that you can play using your fingertips via your webcam. This project uses **MediaPipe** for hand tracking, **OpenCV** for visualization, and **Pygame** for audio playback.

## 🚀 Features

- Detects all five fingertips using your webcam.
- Plays corresponding musical notes when your fingertips hover over virtual keys.
- Uses real-time hand tracking powered by **MediaPipe**.
- Customizable with your own `.mp3` sound files.

## 🖼️ Demo

> *(Add a GIF or link to a video demo here if you have one.)*

## 📁 Project Structure

```
virtual_keyboard/
│
├── assets/              # Contains all the .mp3 sound files
│   ├── a_note(c6).mp3
│   ├── b_note(a6).mp3
│   ├── ...
│
├── env/                 # Your Python virtual environment (not needed on GitHub)
│
├── main.py              # Main application script
├── requirements.txt     # Required Python packages
└── README.md            # This documentation file
```

## 🛠️ Installation & Usage

1. **Clone the repository:**

```bash
git clone https://github.com/Yash29739/Virtua_keyboard.git
cd Virtua_keyboard
```

2. **(Optional) Create a virtual environment:**

```bash
python -m venv env
env\Scripts\activate         # On Windows
# OR
source env/bin/activate      # On macOS/Linux
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the application:**

```bash
python main.py
```

5. **Exit:**
Press `q` on your keyboard to close the application window.

## 📦 Dependencies

- `opencv-python`
- `mediapipe`
- `pygame`

Install manually if needed:
```bash
pip install opencv-python mediapipe pygame
```

## 🎵 Customizing Sounds

You can replace the `.mp3` files inside the `assets/` folder with your own sounds. Just make sure the filenames match those referenced in `main.py`.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

Made with ❤️ by [Yash29739](https://github.com/Yash29739)
