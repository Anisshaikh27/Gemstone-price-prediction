# 🔮 Gemstone Price Prediction

A machine learning web application that predicts gemstone prices based on their physical characteristics using Random Forest regression. This project demonstrates professional ML deployment practices with secure artifact management.

## 🌟 Features

- **Real-time price prediction** for gemstones
- **Web-based interface** for easy interaction
- **Professional ML pipeline** with MLflow tracking
- **Secure deployment** with S3 model storage
- **Docker containerization** for consistent deployments
- **Cloud deployment** ready for production

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Local Dev     │    │   AWS S3        │    │   Render Cloud  │
│                 │    │                 │    │                 │
│ • Training      │───▶│ • Model.pkl    │───▶│ • Web App       │
│ • MLflow        │    │ • Preprocessor  │    │ • Docker        │
│ • Data Science  │    │                 │    │ • Auto Deploy   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📁 Project Structure

```
Gemstone-price-prediction/
├── .github/
│   └── workflows/ci.yml
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│  
├── logs/
├── notebook/
│   ├── Gemstone-Price-Prediction.ipynb
│   └── experiments.ipynb
|
|
├── src/   # source code
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_evaluation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── utils.py
│   ├── logger/logger.py
│   ├── exeception/exception.py
│   └── __init__.py
|
├── templates/
│   └── index.html
|
├── .gitignore
├── app.py
├── requirements.txt
├── requirements_dev.txt
├── Dockerfile
├── .dockerignore
├── template.py
└── README.md
```

## 🔧 Technology Stack

- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Web Framework**: Flask
- **Model Tracking**: MLflow
- **Storage**: AWS S3
- **Containerization**: Docker
- **Deployment**: Render
- **Version Control**: Git
- **Data versioning**: DVC
- **Environment Management**: Conda
- **Testing**: pytest
- **Linting**: flake8
- **Deployment** : render

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Conda (optional, for environment management)
- Docker (optional, for containerization)
- AWS Account (for S3 storage)
- Git

### 1. Clone Repository

```bash
git clone https://github.com/Anisshaikh27/Gemstone-price-prediction.git
cd gemstone-price-prediction
```

### 2. Set Up Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
# Copy environment template
AWS_ACCESS_KEY_ID=xxxxxxxx
AWS_DEFAULT_REGION=xxxxxxxx
S3_BUCKET_NAME=xxxxxxxx
S3_FILE_KEY=xxxxxxxx
DOCKER_USERNAME=xxxxxxxx
DOCKER_PASSWORD=xxxxxxxx
RENDER_SERVICE_ID=xxxxxxxx
RENDER_API_KEY=xxxxxxxx
PORT=xxxxxxxx
FLASK_ENV=production

```

## 🎯 Model Training (Local Development)

### 1. Prepare Your Data

```bash
# Place your training data in data/ folder
mkdir -p data
# Add your gemstone_data.csv file here
```

### 2. Start MLflow Tracking

```bash
# Terminal 1: Start MLflow server
mlflow server --host 0.0.0.0 --port 5000

# Access MLflow UI at: http://localhost:5000
```

### 3. Train the Model

```bash
# Terminal 2: Run training pipeline
python src/pipeline/training_pipeline.py

# This will:
# ✅ Load and preprocess data
# ✅ Train Random Forest model
# ✅ Log metrics to MLflow
# ✅ Save artifacts to artifacts/ folder
```


## 🏃‍♂️ Running Locally

### Option 1: Direct Python

```bash


# Start Flask app
python app.py

# Access app at: http://localhost:PORT
```

### Option 2: Docker (Recommended)

```bash
# Build Docker image
docker build -t gemstone-app .

# Run container
docker run -p 5000:5000 \
  -e AWS_ACCESS_KEY_ID=your_key \
  -e AWS_SECRET_ACCESS_KEY=your_secret \
  -e AWS_DEFAULT_REGION=us-east-1 \
  gemstone-app

# Access app at: http://localhost:5000
```

## 🌐 Production Deployment

### Deploy to Render

1. **Push to GitHub**:
```bash
# Only push code, not data or models
git add .
git commit -m "Deploy to production"
git push origin main
```

2. **Configure Render**:
   - Connect your GitHub repository
   - Set build command: `docker build -t gemstone-app .`
   - Set start command: `docker run -p 5000:5000 gemstone-app`

3. **Set Environment Variables in Render**:
   ```
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_key
   AWS_DEFAULT_REGION=us-east-1
   S3_BUCKET_NAME=your-gemstone-model-bucket
   ```

4. **Deploy**: Render will automatically build and deploy your app!

## 📊 API Usage

### Health Check
```bash
curl -X GET https://your-app.onrender.com/health
```

### Make Prediction
```bash
curl -X POST https://your-app.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "carat": 1.0,
    "depth": 61.5,
    "table": 55.0,
    "x": 6.3,
    "y": 6.54,
    "z": 4.0,
    "cut": "Fair",
    "color": "D",
    "clarity": "I1"
  }'
```

**Response**:
```json
{
  "predicted_price": 4521.32,
  "status": "success"
}
```

## 🔐 Security Features

- **Data Privacy**: Training data never leaves your local machine
- **Secure Storage**: Models stored in private S3 bucket
- **Environment Variables**: Sensitive credentials not in code
- **Access Control**: AWS IAM for proper permissions

## 🛠️ Development Commands

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests (if you have them)
python -m pytest tests/

# Format code
black src/
flake8 src/

# Start development server
python src/app.py
```

### Docker Development
```bash
# Build development image
docker build -t gemstone-app:dev .

# Run with volume mounting for development
docker run -p 5000:5000 -v $(pwd)/src:/app/src gemstone-app:dev

# View logs
docker logs <container_id>

# Shell into container
docker exec -it <container_id> /bin/bash
```

### MLflow Commands
```bash
# Start MLflow server
mlflow server --host 0.0.0.0 --port 5000

# Run experiment
mlflow run . -P alpha=0.5

# View experiments
mlflow ui

# Compare models
mlflow models serve -m models:/gemstone_model/1 -p 5001
```

## 📈 Model Performance

- **Algorithm**: Random Forest Regressor
- **Features**: Carat, Depth, Table, X, Y, Z, Cut, Color, Clarity
- **Metrics**: RMSE, MAE, R²
- **Preprocessing**: StandardScaler + LabelEncoder

## 🚨 Troubleshooting

### Common Issues

1. **"Model not found" error**:
   ```bash
   # Download models from S3
   python src/download_model.py
   ```

2. **AWS credentials error**:
   ```bash
   # Check environment variables
   echo $AWS_ACCESS_KEY_ID
   
   # Or set them explicitly
   export AWS_ACCESS_KEY_ID=your_key
   export AWS_SECRET_ACCESS_KEY=your_secret
   ```

3. **Docker build fails**:
   ```bash
   # Clean Docker cache
   docker system prune -a
   
   # Rebuild without cache
   docker build --no-cache -t gemstone-app .
   ```

4. **MLflow tracking issues**:
   ```bash
   # Check MLflow server
   curl http://localhost:5000
   
   # Set tracking URI
   export MLFLOW_TRACKING_URI=http://localhost:5000
   ```

### Debug Mode

```bash
# Run Flask in debug mode
export FLASK_ENV=development
export FLASK_DEBUG=1
python src/app.py
```

## 🔄 Model Updates

### Update Workflow

1. **Retrain Model**:
```bash
python src/train.py
```

2. **Upload New Model**:
```bash
python src/upload_to_s3.py
```

3. **Redeploy App**:
```bash
# Render will automatically rebuild and download new model
git commit -m "Update model"
git push origin main
```

## 📚 Additional Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Docker Documentation](https://docs.docker.com/)
- [Render Documentation](https://render.com/docs)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Anis Shaikh**
- GitHub: [@Anisshaikh27](https://github.com/Anisshaikh27)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Dataset source: [Mention your data source]
- Inspiration from various ML deployment tutorials
- Thanks to the open-source community

---

**⭐ Star this repository if you found it helpful!**

## 📝 Notes

- This project uses S3 for model storage to keep training data secure
- MLflow is used for experiment tracking and model management
- Docker ensures consistent deployments across environments
- The architecture separates training from serving for production scalability

For any questions or issues, please open an issue in the GitHub repository or contact the maintainer.