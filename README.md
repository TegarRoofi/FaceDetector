## 🧠 Face Detection with Python

A simple face detection project using **Python** and **OpenCV**, running in a virtual environment (`venv`). The app detects faces from a webcam in real-time and draws a bounding box around them.

### 📸 Features

* Real-time face detection from webcam
* Uses Haar Cascade Classifier (`face_reff.xml`)
* Press `q` to quit
* Lightweight and beginner-friendly

### 🛠️ Built With

* Python 3.x
* OpenCV
* Haar Cascade XML file

### 📁 Project Structure

```
project-folder/
├── face_reff.xml          # Haar cascade for face detection
├── main.py                # Main face detection script
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

### 🚀 How to Run

1. **Clone the repo**:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Set up virtual environment**:

```bash
# Create venv if not created
python -m venv venv

# Activate venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run the app**:

```bash
python main.py
```

5. **Press `q` to exit the app.**

### ⚠️ Notes

* Ensure `face_reff.xml` is in the same directory as `main.py`.
* If your webcam is not detected, make sure it’s not being used by another application.

### 🧪 Future Improvements

* Add eye or smile detection
* Save detected faces to a database
* Implement face login system
