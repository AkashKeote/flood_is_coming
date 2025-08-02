# 🌊 Flood Management System - Mumbai

A comprehensive flood monitoring and prediction system designed specifically for Mumbai. Built with Flutter for cross-platform compatibility (Web, Android, iOS).

## 🚀 Live Demo

**[View Live Web App](https://your-github-username.github.io/flood-management-system/)**

## ✨ Features

### 🎯 Core Features
- **Real-time Flood Monitoring**: Live water level tracking and risk assessment
- **AI-Powered Prediction**: Advanced flood risk analysis using machine learning
- **Interactive Map**: Google Maps integration with flood-prone areas and evacuation routes
- **Emergency Response**: Quick access to emergency contacts and safety guidelines
- **User Dashboard**: Personalized flood alerts and status updates

### 📱 Platform Support
- **Web**: Responsive design optimized for desktop, tablet, and mobile browsers
- **Android**: Native Android app with full feature support
- **iOS**: Native iOS app with platform-specific optimizations

### 🎨 UI/UX Features
- **Modern Design**: Clean, professional interface with pastel color scheme
- **Responsive Layout**: Adapts seamlessly across all screen sizes
- **Smooth Animations**: Engaging user experience with Lottie animations
- **Accessibility**: Built with accessibility best practices

## 🛠️ Technology Stack

- **Frontend**: Flutter 3.x
- **Maps**: Google Maps Platform
- **Animations**: Lottie, Flutter Animate
- **UI**: Material Design 3, Cupertino
- **State Management**: Flutter State Management
- **Web Hosting**: GitHub Pages

## 📦 Installation

### Prerequisites
- Flutter SDK (3.0 or higher)
- Dart SDK
- Android Studio / VS Code
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/flood-management-system.git
   cd flood-management-system
   ```

2. **Install dependencies**
   ```bash
   flutter pub get
   ```

3. **Configure Google Maps API**
   - Get a Google Maps API key from [Google Cloud Console](https://console.cloud.google.com/)
   - Enable Maps SDK for Android/iOS and Directions API
   - Add your API key to `android/app/src/main/AndroidManifest.xml`

4. **Run the app**
   ```bash
   # For web
   flutter run -d chrome
   
   # For Android
   flutter run -d android
   
   # For iOS
   flutter run -d ios
   ```

## 🌐 Web Deployment

### Build for Web
```bash
flutter build web --release
```

### Deploy to GitHub Pages

1. **Create a new repository** on GitHub named `flood-management-system`

2. **Push your code**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

3. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Set source to "GitHub Actions"
   - Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    
    - uses: subosito/flutter-action@v2
      with:
        flutter-version: '3.16.0'
        channel: 'stable'
    
    - run: flutter pub get
    - run: flutter build web --release
    
    - name: Deploy
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./build/web
```

4. **Your app will be available at**: `https://your-username.github.io/flood-management-system/`

## 📱 Mobile App Build

### Android APK
```bash
flutter build apk --release
```

### iOS App Store
```bash
flutter build ios --release
```

## 🗺️ Map Features

- **Flood-Prone Areas**: Marked locations with risk levels
- **Evacuation Routes**: Safe paths to shelters
- **Water Level Monitoring**: Real-time drainage and river levels
- **Emergency Shelters**: Nearby safe locations

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:
```
GOOGLE_MAPS_API_KEY=your_api_key_here
```

### API Keys Setup
1. **Google Maps Platform**:
   - Enable Maps SDK for Android
   - Enable Maps SDK for iOS
   - Enable Directions API
   - Add billing information

2. **Android Configuration**:
   - Add API key to `android/app/src/main/AndroidManifest.xml`
   - Configure permissions for location access

## 📊 Data Sources

- **Mumbai Flood Risk Dataset**: Professional dataset with coordinates and risk levels
- **Real-time Weather Data**: Integration with weather APIs
- **Water Level Sensors**: IoT sensor data integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Maps Platform for mapping services
- Flutter team for the amazing framework
- Mumbai Municipal Corporation for flood data
- Open source community for various packages

## 📞 Support

For support, email support@floodmanagement.com or create an issue in this repository.

---

**Stay Safe • Stay Informed** 🌊
