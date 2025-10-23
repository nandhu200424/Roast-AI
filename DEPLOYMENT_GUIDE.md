# 🚀 Limitly - Roast AI Deployment Guide

Complete step-by-step guide to deploy your Limitly roast AI chatbot.

## 📋 Prerequisites

- Python 3.8+ installed
- Git installed
- Groq API key from [Groq Console](https://console.groq.com/)
- Basic terminal/command line knowledge

## 🏗️ Local Development Setup

### Step 1: Clone and Setup Project

```bash
# Clone the repository (if using git)
git clone <your-repo-url>
cd roast-ai

# Or if you have the files locally, navigate to the directory
cd roast-ai
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Groq API Key

```bash
# Create secrets directory
mkdir -p .streamlit

# Create secrets file
nano .streamlit/secrets.toml
```

Fill in your `.streamlit/secrets.toml` file:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### Step 5: Test the Application

```bash
# Activate virtual environment
source venv/bin/activate

# Start the app
streamlit run app.py
```

Visit:
- App URL: http://localhost:8501
- Network URL: http://192.168.0.12:8501

## 🌐 Production Deployment Options

### Option 1: Streamlit Cloud Deployment

#### Step 1: Prepare for Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub account
4. Deploy your app

#### Step 2: Configure Secrets

In Streamlit Cloud dashboard:
1. Go to your app settings
2. Add secrets:
```
GROQ_API_KEY = "your_groq_api_key_here"
```

### Option 2: Heroku Deployment

#### Step 1: Prepare for Heroku

Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

Create `setup.sh`:
```bash
mkdir -p ~/.streamlit
echo "[server]" > ~/.streamlit/config.toml
echo "headless = true" >> ~/.streamlit/config.toml
echo "port = $PORT" >> ~/.streamlit/config.toml
echo "enableCORS = false" >> ~/.streamlit/config.toml
```

#### Step 2: Deploy to Heroku

```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login to Heroku
heroku login

# Create Heroku app
heroku create your-roast-ai-app

# Set environment variables
heroku config:set GROQ_API_KEY=your_api_key_here

# Deploy
git add .
git commit -m "Deploy Roast AI"
git push heroku main
```

### Option 3: Railway Deployment

#### Step 1: Prepare for Railway

Create `railway.json`:
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "streamlit run app.py --server.port=$PORT --server.address=0.0.0.0",
    "healthcheckPath": "/"
  }
}
```

#### Step 2: Deploy to Railway

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Deploy
railway up
```

### Option 4: Docker Deployment

#### Step 1: Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Step 2: Build and Run

```bash
# Build Docker image
docker build -t roast-ai .

# Run container
docker run -p 8501:8501 -e GROQ_API_KEY=your_key_here roast-ai
```

## 🔧 Environment Configuration

### Required Environment Variables

```toml
# Groq API Key
GROQ_API_KEY=your_groq_api_key_here
```

## 🚨 Security Considerations

### Production Security Checklist

- [ ] Set up proper API key management
- [ ] Use environment variables for all secrets
- [ ] Enable HTTPS/SSL
- [ ] Set up monitoring and logging
- [ ] Regular security updates

### API Key Security

```bash
# Never commit API keys to git
echo ".streamlit/secrets.toml" >> .gitignore
echo "*.key" >> .gitignore
echo "secrets/" >> .gitignore
```

## 📊 Monitoring and Maintenance

### Health Checks

```bash
# Check if app is running
curl http://localhost:8501
```

### Logs

```bash
# View application logs (if using systemd)
journalctl -u your-app-name -f

# View Docker logs
docker logs your-container-name
```

## 🔄 Updates and Maintenance

### Updating the Application

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt

# Restart service
# (depends on your deployment method)
```

### Backup Strategy

```bash
# Backup secrets
cp .streamlit/secrets.toml backup/secrets_$(date +%Y%m%d).backup
```

## 🆘 Troubleshooting

### Common Issues

**App won't start:**
```bash
# Check if port is in use
sudo netstat -tlnp | grep :8501

# Check logs
# (depends on your deployment method)
```

**API key issues:**
- Verify API key is correct
- Check if API key has proper permissions
- Ensure secrets are properly configured

**Dependencies issues:**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Getting Help

1. Check the logs first
2. Verify all environment variables
3. Test API endpoints manually
4. Check network connectivity
5. Review security settings

## 🎉 Success!

Once deployed, your Limitly roast AI should be accessible at your domain and ready to roast users! 🔥

Remember to:
- Monitor usage and performance
- Keep dependencies updated
- Backup important data
- Monitor for any security issues
