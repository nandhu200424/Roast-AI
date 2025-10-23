#  Limitly - Roast AI

A savage AI-powered chatbot that destroys everything you say with brutal honesty and dark humor. Built with Streamlit frontend and Groq API integration.

##  Features

- **AI-Powered Roasts**: Uses Groq API with Llama 3.3 70B to generate savage roasts
- **Interactive Web Interface**: Beautiful Streamlit frontend with animated doodles
- **Real-time Chat**: Instant responses with custom styling and animations
- **Roast Intensity Control**: Adjustable slider to control how savage the roasts are
- **Live Statistics**: Track total roasts and messages in real-time
- **Animated UI**: Bouncing emojis and interactive elements
- **Custom Styling**: Gradient backgrounds and professional design
- **Responsive Design**: Works on desktop and mobile devices

## 📁 Project Structure

```
roast-ai/
├── app.py                  # Streamlit frontend application
├── requirements.txt        # Python dependencies
├── system_prompt.txt      # AI roast prompt and guidelines
├── .streamlit/
│   └── secrets.toml      # Groq API key configuration
├── .gitignore             # Git ignore file for security
├── README.md              # This file
└── DEPLOYMENT_GUIDE.md    # Complete deployment instructions
```

##  Quick Start

### 1. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt
```

### 2. Configure Groq API Key

```bash
# Create secrets file
mkdir -p .streamlit
```

Edit `.streamlit/secrets.toml` and add your Groq API key:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### 3. Run the Application

```bash
# Activate virtual environment
source venv/bin/activate

# Start the app
streamlit run app.py
```

### 4. Access the Application

- **App URL**: http://localhost:8501
- **Network URL**: http://192.168.0.12:8501

##  Documentation

- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Complete deployment instructions for production
- **[system_prompt.txt](system_prompt.txt)** - AI roast prompt and guidelines

##  Configuration

### Groq API Integration

The application uses Groq API with Llama 3.3 70B model for fast, high-quality roasts.

#### Setup Groq API
1. Get your API key from [Groq Console](https://console.groq.com/)
2. Add it to `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### UI Customization

The app includes several customizable elements:
- **Roast Intensity Slider**: Adjust how savage the roasts are (1-10)
- **Animated Doodles**: Bouncing emojis that change with each response
- **Custom Styling**: Gradient backgrounds and professional design
- **Live Statistics**: Real-time tracking of roasts and messages

##  Features

- **Real-time Chat**: Instant responses with custom styling
- **Interactive UI**: Animated elements and smooth transitions
- **Roast Statistics**: Track your roasting sessions
- **Customizable Intensity**: Control how savage the AI gets
- **Mobile Responsive**: Works on all devices

##  How to Use

1. **Start the app**: Run `streamlit run app.py`
2. **Open your browser**: Go to `http://localhost:8501`
3. **Adjust settings**: Use the sidebar to control roast intensity
4. **Start chatting**: Type anything and get roasted!
5. **Track stats**: Monitor your roasting sessions in real-time

##  Example Interactions

Try these examples to see Limitly in action:
- "I'm amazing at everything"
- "I spent too much money"
- "I'm really smart"
- "I didn't do anything today"
- "I'm the best at coding"

##  Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

##  Have Fun!

Remember, this is all in good fun! The roasts are meant to be humorous and light-hearted. Enjoy getting roasted! 😈🔥💀
