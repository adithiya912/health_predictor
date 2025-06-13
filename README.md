HealthGuard - AI-Powered Health Risk Assessment Platform
Overview
HealthGuard is a comprehensive web-based health assessment platform that uses machine learning to predict health risks for heart disease and diabetes. The application provides users with personalized risk assessments based on their health parameters and lifestyle factors, offering actionable recommendations for maintaining optimal health.

Features
🏥 Heart Disease Risk Assessment
Comprehensive evaluation based on 13 clinical parameters
User-friendly questionnaire with intuitive options
Risk prediction using trained logistic regression model
Personalized recommendations based on risk level
🩺 Diabetes Risk Assessment
8-parameter evaluation system
Lifestyle and health factor analysis
SVM-based machine learning prediction
Tailored health guidance and prevention strategies
📊 Interactive Results Dashboard
Visual risk representation with dynamic charts
Color-coded risk levels (Low/High)
Detailed recommendations list
Professional medical disclaimer
🎨 Modern User Interface
Responsive design for all devices
Clean, medical-grade aesthetic
Smooth animations and transitions
Accessible form controls and navigation
Technology Stack
Frontend
HTML5/CSS3 - Modern web standards
JavaScript (ES6+) - Interactive functionality
Chart.js - Data visualization
Responsive Design - Mobile-first approach
Backend
Node.js - Server runtime
Express.js - Web framework
CORS - Cross-origin resource sharing
Body-parser - Request parsing
Machine Learning
Python 3 - ML runtime environment
scikit-learn - Machine learning algorithms
NumPy - Numerical computing
Pandas - Data manipulation
Pickle - Model serialization
Installation & Setup
Prerequisites
Node.js (v14 or higher)
Python 3.7+
npm or yarn package manager
Installation Steps
Clone the repository


git clone https://github.com/yourusername/healthguard.git
cd healthguard
Install Node.js dependencies


npm install
Install Python dependencies


pip install numpy pandas scikit-learn
Train the machine learning models


python train_model.py
python train_diabetes_model.py
Start the application


npm start
Access the application

Open your browser and navigate to http://localhost:3000
Usage
Heart Disease Assessment
Navigate to the "Heart Health" tab
Fill out the comprehensive health questionnaire
Submit the form to receive your risk assessment
Review personalized recommendations
Diabetes Risk Assessment
Switch to the "Diabetes Risk" tab
Complete the lifestyle and health parameter form
Get your diabetes risk prediction
Follow the provided health guidance
Model Information
Heart Disease Model
Algorithm: Logistic Regression
Features: 13 clinical parameters
Dataset: Heart disease clinical data
Accuracy: Optimized for clinical relevance
Diabetes Model
Algorithm: Support Vector Machine (SVM)
Features: 8 health and lifestyle parameters
Dataset: Diabetes health indicators
Preprocessing: StandardScaler normalization
API Endpoints
POST /predict/heart
Predicts heart disease risk based on clinical parameters.

Request Body:


{
  "age": 45,
  "sex": 1,
  "chestPain": 2,
  "bloodPressure": 130,
  "cholesterol": 220,
  "fastingBloodSugar": 0,
  "ekgResults": 0,
  "heartRate": 150,
  "exerciseAngina": 0,
  "stDepression": 1,
  "stSlope": 1,
  "numVessels": 0,
  "thallium": 2
}
POST /predict/diabetes
Predicts diabetes risk based on health parameters.

Request Body:


{
  "pregnancies": 2,
  "glucose": 120,
  "bloodPressure": 80,
  "skinThickness": 25,
  "insulin": 100,
  "bmi": 27,
  "diabetesPedigree": 0.3,
  "age": 35
}
File Structure

healthguard/
├── public/
│   ├── index.html          # Main HTML file
│   ├── styles.css          # CSS styling
│   └── script.js           # Frontend JavaScript
├── src/                    # React components (if applicable)
├── models/
│   ├── model.pkl           # Heart disease model
│   ├── diabetes_model.pkl  # Diabetes model
│   └── diabetes_scaler.pkl # Feature scaler
├── data/
│   └── heart_disease_data.csv # Training data
├── scripts/
│   ├── predict.py          # Heart disease prediction
│   ├── predict_diabetes.py # Diabetes prediction
│   ├── train_model.py      # Heart model training
│   └── train_diabetes_model.py # Diabetes model training
├── index.js                # Express server
├── package.json            # Node.js dependencies
└── README.md              # Project documentation
Contributing
Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
Disclaimer
Important Medical Disclaimer: This application is designed for educational and informational purposes only. The health risk assessments provided are not intended to replace professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns and before making any health-related decisions.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Support
For support, questions, or contributions, please open an issue on GitHub or contact the development team.

HealthGuard - Empowering informed health decisions through AI-powered risk assessment.
