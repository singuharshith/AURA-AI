# 🎵 AURA AI - Intelligent Voice Assistant

<div align="center">

[![React](https://img.shields.io/badge/React-19.0-blue?logo=react)](https://react.dev)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Latest-lightgrey?logo=flask)](https://flask.palletsprojects.com)
[![Vite](https://img.shields.io/badge/Vite-6.1-purple?logo=vite)](https://vitejs.dev)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

*A modern, real-time voice assistant application with immersive audio visualization and intelligent conversation management.*

[Features](#-features) • [Getting Started](#-getting-started) • [Project Structure](#-project-structure) • [API Documentation](#-api-documentation) • [Contributing](#-contributing)

</div>

---

## 🌟 Overview

**Aura AI** is a sophisticated voice assistant platform that combines cutting-edge web technologies with powerful backend processing. It delivers real-time audio visualization, intelligent conversation handling, and seamless user interaction through a modern React-based interface powered by a Python Flask backend.

Perfect for:
- Building AI-driven voice applications
- Creating immersive voice interaction experiences
- Developing intelligent call management systems
- Prototyping voice-enabled platforms

---

## ✨ Features

### 🎙️ Voice Interaction
- **Real-time Voice Input/Output** - Seamless bidirectional audio communication
- **Audio Visualization** - Dynamic visual feedback synchronized with audio levels
- **Assistant Speech Detection** - Real-time indicator showing when the AI is speaking
- **Volume Level Monitoring** - Live volume tracking and display

### 📞 Call Management
- **Active Call Details** - Display comprehensive call information during sessions
- **Call History** - Track and retrieve all past call records
- **Call Analytics** - Access detailed call metadata and results
- **Session Persistence** - Maintain call states across interactions

### 🎨 User Experience
- **Modern UI** - Built with React 19 for optimal performance
- **Real-time Updates** - Instant feedback and state management
- **Responsive Design** - Works seamlessly across devices
- **Smooth Animations** - Professional visual feedback

### 🔌 Integration
- **Vapi AI Integration** - Powered by Vapi's intelligent voice API
- **REST API Backend** - Flexible Python Flask server for custom logic
- **CORS Support** - Secure cross-origin requests
- **Environment Configuration** - Easy setup with .env files

---

## 🛠️ Tech Stack

### Frontend
- **React 19.0** - Modern UI library with hooks and concurrent features
- **Vite 6.1** - Lightning-fast build tool and dev server
- **Vapi AI SDK** - @vapi-ai/web for voice assistant integration
- **CSS3** - Styled animations and responsive layouts
- **ESLint** - Code quality and consistency

### Backend
- **Python 3.8+** - Core backend language
- **Flask** - Lightweight web framework
- **Requests** - HTTP client for API calls
- **Flask-CORS** - Cross-Origin Resource Sharing support
- **python-dotenv** - Environment variable management

### Development Tools
- **npm** - Package management
- **Git** - Version control
- **VS Code** - Recommended IDE

---

## 🚀 Getting Started

### Prerequisites
- **Node.js 16+** and npm
- **Python 3.8+** and pip
- **Vapi API Key** - Get it from [vapi.ai](https://vapi.ai)
- **Git** for version control

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/singuharshith/AURA-AI.git
cd AURA-AI
```

#### 2. Frontend Setup
```bash
cd AURA-AI

# Install dependencies
npm install

# Create environment file
cp .env.example .env

# Add your Vapi API Key to .env
# VITE_VAPI_API_KEY=your_api_key_here
```

#### 3. Backend Setup
```bash
cd backend

# Create Python virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Add your Vapi API Key to .env
# VAPI_API_KEY=your_api_key_here
```

### Running the Application

#### Start the Frontend (Terminal 1)
```bash
cd AURA-AI
npm run dev
```
The frontend will be available at `http://localhost:5173`

#### Start the Backend (Terminal 2)
```bash
cd backend
python main.py
```
The backend will be available at `http://localhost:5000`

### Development Commands

**Frontend:**
```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run preview  # Preview production build
npm run lint     # Run ESLint
```

**Backend:**
```bash
python main.py   # Run Flask server
```

---

## 📁 Project Structure

```
AURA-AI/
├── AURA-AI/                          # Frontend (React + Vite)
│   ├── src/
│   │   ├── main.jsx                 # Entry point
│   │   ├── App.jsx                  # Main application component
│   │   ├── ai.js                    # Vapi AI integration
│   │   ├── index.css                # Global styles
│   │   ├── AudioVisualizer.jsx      # Audio visualization component
│   │   └── call/
│   │       ├── ActiveCallDetails.jsx    # Call information display
│   │       ├── AssistantSpeechIndicator.jsx  # Speech detection indicator
│   │       └── VolumeLevel.jsx          # Volume level display
│   ├── public/
│   │   └── vite.svg
│   ├── index.html                   # HTML template
│   ├── package.json                 # Frontend dependencies
│   ├── vite.config.js               # Vite configuration
│   ├── eslint.config.js             # ESLint rules
│   ├── .gitignore                   # Git ignore rules
│   └── README.md                    # Frontend documentation
│
├── backend/                          # Backend (Python + Flask)
│   ├── main.py                      # Flask application & routes
│   ├── requirements.txt             # Python dependencies
│   ├── .env                         # Environment variables
│   └── .env.example                 # Environment template
│
├── AURA-AI.code-workspace           # VS Code workspace configuration
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

---

## 🔌 API Documentation

### Frontend API (Flask Backend)

#### Get Call Details
```http
GET /call-details?call_id=<call_id>
```

**Response:**
```json
{
  "call_id": "string",
  "duration": "number",
  "status": "string",
  "transcript": "string",
  "metadata": {}
}
```

#### Get All Calls
```http
GET /all-calls
```

**Response:**
```json
[
  {
    "call_id": "string",
    "timestamp": "datetime",
    "duration": "number"
  }
]
```

### Vapi AI Integration

The frontend integrates with **Vapi AI API** for intelligent voice conversations:

- **Start Call** - Initiates voice assistant
- **Stop Call** - Ends the conversation
- **Real-time Events** - Audio data, speech detection, call metrics

Refer to [Vapi Documentation](https://docs.vapi.ai) for detailed integration details.

---

## 🎯 Key Components

### AudioVisualizer.jsx
Renders real-time audio visualization synchronized with voice input/output.

### ActiveCallDetails.jsx
Displays current call information including:
- Call duration
- Agent status
- User information
- Real-time transcript

### AssistantSpeechIndicator.jsx
Visual indicator showing when the AI assistant is actively speaking.

### VolumeLevel.jsx
Real-time volume level meter for audio monitoring.

---

## 🔐 Environment Variables

### Frontend (.env)
```env
VITE_VAPI_API_KEY=your_vapi_api_key
VITE_API_BASE_URL=http://localhost:5000
```

### Backend (.env)
```env
VAPI_API_KEY=your_vapi_api_key
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
```

> ⚠️ **Never commit .env files!** Use `.env.example` as a template.

---

## 📦 Dependencies

### Frontend
```json
{
  "@vapi-ai/web": "^2.2.2",
  "react": "^19.0.0",
  "react-dom": "^19.0.0"
}
```

### Backend
```
requests>=2.28.0
Flask>=2.0.0
python-dotenv>=0.19.0
flask-cors>=3.0.10
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the Repository** - Create your own copy
2. **Create a Feature Branch** - `git checkout -b feature/amazing-feature`
3. **Commit Changes** - `git commit -m 'Add amazing feature'`
4. **Push to Branch** - `git push origin feature/amazing-feature`
5. **Open a Pull Request** - Describe your changes

### Code Style
- Follow ESLint rules for JavaScript/React
- Use PEP 8 for Python code
- Add comments for complex logic
- Update documentation as needed

---

## 📝 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 🙋 Support & Questions

- 📧 **Email**: harshith@example.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/singuharshith/AURA-AI/issues)
- 📚 **Documentation**: Check the [docs](./docs) folder
- 💬 **Discussions**: Join our community discussions

---

## 🚀 Future Enhancements

- [ ] Multi-language support
- [ ] Advanced conversation analytics
- [ ] Custom voice profiles
- [ ] Integration with more AI providers
- [ ] Mobile app version
- [ ] Real-time transcription display
- [ ] Recording and playback features
- [ ] User authentication system

---

## 🙏 Acknowledgments

- [Vapi AI](https://vapi.ai) - For powerful voice assistant APIs
- [React](https://react.dev) - For the amazing UI library
- [Vite](https://vitejs.dev) - For the blazing-fast build tool
- [Flask](https://flask.palletsprojects.com) - For the lightweight backend framework

---

<div align="center">

**Made with ❤️ by the Aura AI Team**

[⬆ Back to Top](#-aura-ai---intelligent-voice-assistant)

</div>
