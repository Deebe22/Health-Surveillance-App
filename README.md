# health_surveillance_app

A new Flutter project.

# Smart Health Surveillance and Early Warning System

A Flutter-based health monitoring application that helps detect and monitor water-borne disease outbreaks through community reporting, GPS tracking, symptom collection, and health surveillance. The system supports health workers, clinic staff, and volunteers in reporting disease cases and identifying potential outbreak hotspots.

## Features

* User Registration and Login
* Role-Based Access

  * Clinic Staff
  * ASHA Worker
  * Community Volunteer
  * Public Community User
* Health Report Submission
* GPS Location Tracking
* Water Source Monitoring
* Symptom Reporting
* Image Upload for Evidence
* Reports History
* Password Reset
* Offline Data Storage using SharedPreferences
* Community Health Surveillance Dashboard

## Project Objective

The objective of this project is to provide an early warning system for water-borne diseases by collecting and analyzing health reports from communities. The system helps health authorities identify disease-prone areas and respond quickly to potential outbreaks.

## Technologies Used

* Flutter
* Dart
* SharedPreferences
* Geolocator
* Image Picker
* Material UI Components

## Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Smart-Health-Surveillance-System.git

cd Smart-Health-Surveillance-System
```

### Step 2: Install Dependencies

```bash
flutter pub get
```

### Step 3: Run the Application

```bash
flutter run
```

## Application Workflow

1. User creates an account.
2. User logs in using username, password, and role.
3. User submits a health report.
4. Report includes:

   * Village Name
   * Number of Affected People
   * Water Source
   * Symptoms
   * GPS Coordinates
   * Photo Evidence
5. Reports are stored and displayed in Reports History.
6. Health officials can monitor disease trends and outbreak-prone locations.

## Future Enhancements

* AI Disease Outbreak Prediction
* Water Quality Sensor Integration (IoT)
* Real-Time Alerts and Notifications
* Heatmap Visualization
* Firebase Cloud Storage
* Analytics Dashboard
* Multilingual Support
* Offline Syncing

## Folder Structure

```text
/lib
│
├── data/
│   └── app_data.dart
│
├── models/
│   ├── app_user.dart
│   └── health_report.dart
│
├── screens/
│   ├── login_screen.dart
│   ├── signup_screen.dart
│   ├── forgot_password_screen.dart
│   ├── dashboard_screen.dart
│   ├── report_form_screen.dart
│   └── reports_history_screen.dart
│
└── main.dart
```

## Screens Included

* Login Screen
* Signup Screen
* Forgot Password Screen
* Dashboard Screen
* New Health Report Screen
* Reports History Screen

## Future AI Module

The future version will use Machine Learning models to:

* Detect disease outbreak patterns
* Predict outbreak risk levels
* Analyze symptom trends
* Generate early warning alerts

