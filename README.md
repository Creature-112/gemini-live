# 🎥 Gemini Live: Real-Time Streaming to Google Gemini

![Gemini Live](https://img.shields.io/badge/Gemini_Live-Real--Time_Streaming-blue)

Welcome to the **Gemini Live** repository! This project enables real-time streaming of audio, and optionally video or screen captures, from your local device to Google Gemini using the Live API. With Gemini Live, you can interact with Gemini through both text and voice, supporting conversational AI responses.

This new version features a sleek, modern, and elegant overlay interface that is designed to be non-intrusive and user-friendly.

## 🚀 Features

- **Real-Time Audio Streaming**: Stream audio directly from your device to Google Gemini.
- **Video and Screen Capture Support**: Optionally include video or screen captures in your streams.
- **Conversational AI**: Engage with Gemini using both text and voice, making your interactions more dynamic.
- **Modern Overlay UI**: A minimal and elegant overlay that doesn't interfere with your workflow.
- **Easy Setup**: Simple installation and setup process for quick access.
- **Cross-Platform**: Works on various operating systems, including Windows, macOS, and Linux.

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- An environment variable named `GEMINI_API_KEY` with your Google Gemini API key.

### Required Libraries

You will need to install the following libraries from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 🔧 Usage

1. **Start the Application**: Run the main script to initiate the streaming process.

   ```bash
   python app.py
   ```

2. **Begin Streaming**: Click the circular button to start streaming to Google Gemini. The button's border will turn green to indicate that streaming is active.

3. **Interact with Gemini**: Use your voice to engage with the AI. The AI's responses will appear as pop-up text above the button.

4. **Stop Streaming**: Click the button again to stop streaming.

## 📈 Project Structure

```
gemini-live/
│
├── app.py              # Main application script
├── overlay.py          # The overlay UI
├── gemini.py           # Gemini API integration
├── requirements.txt    # Required Python libraries
├── README.md           # Project documentation
└── sample.env          # Sample environment file
```

## 🌐 Topics

This project covers various topics related to AI and real-time processing:

- gemini
- gemini-2-0-flash
- gemini-2-0-flash-live
- gemini-ai
- gemini-api
- gemini-flash
- google-genai
- google-generative-ai
- live
- live-video-processing
- python
- python-generative-ai
- realtime
- realtime-video-processor
- video-analysis
- pyside6
- overlay

## 🤝 Contributing

We welcome contributions! If you want to help improve Gemini Live, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Create a pull request.

## 📄 License

This project is licensed under the MIT License.

## 💬 Support

If you encounter any issues or have questions, feel free to open an issue in the repository.

## 🎉 Acknowledgments

- Thanks to the Google Gemini team for providing the Live API.
- Special thanks to all contributors and users who provide feedback.

## 🛠️ Tools Used

- Python
- PySide6
- OpenCV
- PyAudio
- Google Gemini API

---

Thank you for your interest in Gemini Live! We look forward to seeing how you use this project to enhance your interactions with Google Gemini. Happy streaming!