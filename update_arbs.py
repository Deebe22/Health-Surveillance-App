import json
import os

def load_json(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

en_additions = {
  "dashboardTitle": "Dashboard",
  "welcome": "Welcome {name}",
  "@welcome": {
    "placeholders": {
      "name": {
        "type": "String"
      }
    }
  },
  "roleLabel": "Role",
  "newReport": "New Report",
  "viewReports": "View Reports",
  "submitHealthReport": "Submit Health Report",
  "reportedBy": "Reported by: {name}",
  "@reportedBy": {
    "placeholders": {
      "name": {
        "type": "String"
      }
    }
  },
  "villageName": "Village Name",
  "enterVillageName": "Enter village name",
  "numberOfAffected": "Number of affected people",
  "enterNumber": "Enter number",
  "waterSource": "Water Source",
  "selectWaterSource": "Select water source",
  "well": "Well",
  "river": "River",
  "tap": "Tap",
  "symptomsTitle": "Symptoms",
  "diarrhea": "Diarrhea",
  "fever": "Fever",
  "vomiting": "Vomiting",
  "stomachPain": "Stomach Pain",
  "gpsPrefix": "GPS",
  "gettingLocation": "Getting location...",
  "refreshLocation": "Refresh Location",
  "uploadPhoto": "Upload Photo",
  "reportSubmittedMsg": "Report Submitted Successfully!",
  "submitReport": "Submit Report",
  "fullName": "Full Name",
  "enterName": "Enter name",
  "email": "Email",
  "enterValidEmail": "Enter valid email",
  "userAlreadyExists": "User already exists",
  "accountCreatedMsg": "Account created successfully",
  "min4Chars": "Min 4 chars",
  "confirmPassword": "Confirm Password",
  "passwordsNotMatch": "Passwords not match",
  "resetPassword": "Reset Password",
  "passwordResetSuccess": "Password reset successful",
  "noAccountFound": "No account found",
  "errorConnecting": "Error connecting to server",
  "newPassword": "New Password",
  "reportsHistory": "Reports History",
  "noReportsYet": "No Reports Yet",
  "nameLabel": "Name",
  "affectedLabel": "Affected",
  "timeLabel": "Time",
  "dashboard": "Dashboard",
  "logout": "Logout",
  "signup": "Sign Up"
}

hi_translations = {
  "dashboardTitle": "डैशबोर्ड",
  "welcome": "स्वागत है {name}",
  "roleLabel": "भूमिका",
  "newReport": "नई रिपोर्ट",
  "viewReports": "रिपोर्ट देखें",
  "submitHealthReport": "स्वास्थ्य रिपोर्ट जमा करें",
  "reportedBy": "द्वारा रिपोर्ट किया गया: {name}",
  "villageName": "गाँव का नाम",
  "enterVillageName": "गाँव का नाम दर्ज करें",
  "numberOfAffected": "प्रभावित लोगों की संख्या",
  "enterNumber": "संख्या दर्ज करें",
  "waterSource": "जल स्रोत",
  "selectWaterSource": "जल स्रोत चुनें",
  "well": "कुआं",
  "river": "नदी",
  "tap": "नल",
  "symptomsTitle": "लक्षण",
  "diarrhea": "दस्त",
  "fever": "बुखार",
  "vomiting": "उल्टी",
  "stomachPain": "पेट दर्द",
  "gpsPrefix": "जीपीएस",
  "gettingLocation": "स्थान प्राप्त कर रहा है...",
  "refreshLocation": "स्थान ताज़ा करें",
  "uploadPhoto": "फोटो अपलोड करें",
  "reportSubmittedMsg": "रिपोर्ट सफलतापूर्वक जमा की गई!",
  "submitReport": "रिपोर्ट जमा करें",
  "fullName": "पूरा नाम",
  "enterName": "नाम दर्ज करें",
  "email": "ईमेल",
  "enterValidEmail": "वैध ईमेल दर्ज करें",
  "userAlreadyExists": "उपयोगकर्ता पहले से मौजूद है",
  "accountCreatedMsg": "खाता सफलतापूर्वक बन गया",
  "min4Chars": "कम से कम 4 अक्षर",
  "confirmPassword": "पासवर्ड की पुष्टि करें",
  "passwordsNotMatch": "पासवर्ड मेल नहीं खाते",
  "resetPassword": "पासवर्ड रीसेट करें",
  "passwordResetSuccess": "पासवर्ड रीसेट सफल",
  "noAccountFound": "कोई खाता नहीं मिला",
  "errorConnecting": "सर्वर से कनेक्ट करने में त्रुटि",
  "newPassword": "नया पासवर्ड",
  "reportsHistory": "रिपोर्ट इतिहास",
  "noReportsYet": "अभी तक कोई रिपोर्ट नहीं",
  "nameLabel": "नाम",
  "affectedLabel": "प्रभावित",
  "timeLabel": "समय",
  "dashboard": "डैशबोर्ड",
  "logout": "लॉग आउट",
  "signup": "साइन अप"
}

ta_translations = {
  "dashboardTitle": "முகப்புப்பலகை",
  "welcome": "வரவேற்கிறோம் {name}",
  "roleLabel": "பங்கு",
  "newReport": "புதிய அறிக்கை",
  "viewReports": "அறிக்கைகளைப் பார்க்கவும்",
  "submitHealthReport": "சுகாதார அறிக்கையை சமர்ப்பிக்கவும்",
  "reportedBy": "அறிக்கையாளர்: {name}",
  "villageName": "கிராமத்தின் பெயர்",
  "enterVillageName": "கிராமத்தின் பெயரை உள்ளிடவும்",
  "numberOfAffected": "பாதிக்கப்பட்டவர்களின் எண்ணிக்கை",
  "enterNumber": "எண்ணை உள்ளிடவும்",
  "waterSource": "நீர் ஆதாரம்",
  "selectWaterSource": "நீர் ஆதாரத்தை தேர்ந்தெடுக்கவும்",
  "well": "கிணறு",
  "river": "நதி",
  "tap": "குழாய்",
  "symptomsTitle": "அறிகுறிகள்",
  "diarrhea": "வயிற்றுப்போக்கு",
  "fever": "காய்ச்சல்",
  "vomiting": "வாந்தி",
  "stomachPain": "வயிற்று வலி",
  "gpsPrefix": "ஜிபிஎஸ்",
  "gettingLocation": "இடத்தை பெறுகிறது...",
  "refreshLocation": "இடத்தை புதுப்பிக்கவும்",
  "uploadPhoto": "புகைப்படத்தை பதிவேற்றவும்",
  "reportSubmittedMsg": "அறிக்கை வெற்றிகரமாக சமர்ப்பிக்கப்பட்டது!",
  "submitReport": "அறிக்கையைச் சமர்ப்பிக்கவும்",
  "fullName": "முழு பெயர்",
  "enterName": "பெயரை உள்ளிடவும்",
  "email": "மின்னஞ்சல்",
  "enterValidEmail": "சரியான மின்னஞ்சலை உள்ளிடவும்",
  "userAlreadyExists": "பயனர் ஏற்கனவே உள்ளார்",
  "accountCreatedMsg": "கணக்கு வெற்றிகரமாக உருவாக்கப்பட்டது",
  "min4Chars": "குறைந்தது 4 எழுத்துக்கள்",
  "confirmPassword": "கடவுச்சொல்லை மீண்டும் உள்ளிடவும்",
  "passwordsNotMatch": "கடவுச்சொற்கள் பொருந்தவில்லை",
  "resetPassword": "கடவுச்சொல்லை மீட்டமை",
  "passwordResetSuccess": "கடவுச்சொல் வெற்றிகரமாக மீட்டமைக்கப்பட்டது",
  "noAccountFound": "கணக்கு எதுவும் கிடைக்கவில்லை",
  "errorConnecting": "சேவையகத்துடன் இணைப்பதில் பிழை",
  "newPassword": "புதிய கடவுச்சொல்",
  "reportsHistory": "அறிக்கைகள் வரலாறு",
  "noReportsYet": "இன்னும் அறிக்கைகள் இல்லை",
  "nameLabel": "பெயர்",
  "affectedLabel": "பாதிக்கப்பட்டவர்கள்",
  "timeLabel": "நேரம்",
  "dashboard": "முகப்புப்பலகை",
  "logout": "வெளியேறு",
  "signup": "பதிவு செய்யவும்"
}

kn_translations = {
  "dashboardTitle": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
  "welcome": "ಸ್ವಾಗತ {name}",
  "roleLabel": "ಪಾತ್ರ",
  "newReport": "ಹೊಸ ವರದಿ",
  "viewReports": "ವರದಿಗಳನ್ನು ನೋಡಿ",
  "submitHealthReport": "ಆರೋಗ್ಯ ವರದಿ ಸಲ್ಲಿಸಿ",
  "reportedBy": "ವರದಿ ಮಾಡಿದವರು: {name}",
  "villageName": "ಗ್ರಾಮದ ಹೆಸರು",
  "enterVillageName": "ಗ್ರಾಮದ ಹೆಸರನ್ನು ನಮೂದಿಸಿ",
  "numberOfAffected": "ಬಾಧಿತರಾದವರ ಸಂಖ್ಯೆ",
  "enterNumber": "ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ",
  "waterSource": "ನೀರಿನ ಮೂಲ",
  "selectWaterSource": "ನೀರಿನ ಮೂಲವನ್ನು ಆಯ್ಕೆಮಾಡಿ",
  "well": "ಬಾವಿ",
  "river": "ನದಿ",
  "tap": "ಟ್ಯಾಪ್",
  "symptomsTitle": "ರೋಗಲಕ್ಷಣಗಳು",
  "diarrhea": "ಅತಿಸಾರ",
  "fever": "ಜ್ವರ",
  "vomiting": "ವಾಂತಿ",
  "stomachPain": "ಹೊಟ್ಟೆ ನೋವು",
  "gpsPrefix": "ಜಿಪಿಎಸ್",
  "gettingLocation": "ಸ್ಥಳವನ್ನು ಪಡೆಯಲಾಗುತ್ತಿದೆ...",
  "refreshLocation": "ಸ್ಥಳವನ್ನು ರಿಫ್ರೆಶ್ ಮಾಡಿ",
  "uploadPhoto": "ಫೋಟೋ ಅಪ್ಲೋಡ್ ಮಾಡಿ",
  "reportSubmittedMsg": "ವರದಿ ಯಶಸ್ವಿಯಾಗಿ ಸಲ್ಲಿಸಲಾಗಿದೆ!",
  "submitReport": "ವರದಿ ಸಲ್ಲಿಸಿ",
  "fullName": "ಪೂರ್ಣ ಹೆಸರು",
  "enterName": "ಹೆಸರನ್ನು ನಮೂದಿಸಿ",
  "email": "ಇಮೇಲ್",
  "enterValidEmail": "ಮಾನ್ಯ ಇಮೇಲ್ ಅನ್ನು ನಮೂದಿಸಿ",
  "userAlreadyExists": "ಬಳಕೆದಾರರು ಈಗಾಗಲೇ ಅಸ್ತಿತ್ವದಲ್ಲಿದ್ದಾರೆ",
  "accountCreatedMsg": "ಖಾತೆ ಯಶಸ್ವಿಯಾಗಿ ರಚಿಸಲಾಗಿದೆ",
  "min4Chars": "ಕನಿಷ್ಠ 4 ಅಕ್ಷರಗಳು",
  "confirmPassword": "ಪಾಸ್ವರ್ಡ್ ದೃಢೀಕರಿಸಿ",
  "passwordsNotMatch": "ಪಾಸ್ವರ್ಡ್ಗಳು ಹೊಂದಿಕೆಯಾಗುವುದಿಲ್ಲ",
  "resetPassword": "ಪಾಸ್ವರ್ಡ್ ಮರುಹೊಂದಿಸಿ",
  "passwordResetSuccess": "ಪಾಸ್ವರ್ಡ್ ಯಶಸ್ವಿಯಾಗಿ ಮರುಹೊಂದಿಸಲಾಗಿದೆ",
  "noAccountFound": "ಯಾವುದೇ ಖಾತೆ ಕಂಡುಬಂದಿಲ್ಲ",
  "errorConnecting": "ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸುವಲ್ಲಿ ದೋಷ",
  "newPassword": "ಹೊಸ ಪಾಸ್ವರ್ಡ್",
  "reportsHistory": "ವರದಿಗಳ ಇತಿಹಾಸ",
  "noReportsYet": "ಇನ್ನೂ ಯಾವುದೇ ವರದಿಗಳಿಲ್ಲ",
  "nameLabel": "ಹೆಸರು",
  "affectedLabel": "ಬಾಧಿತರಾದವರು",
  "timeLabel": "ಸಮಯ",
  "dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
  "logout": "ಲಾಗ್ ಔಟ್",
  "signup": "ಸೈನ್ ಅಪ್"
}

l10n_dir = 'c:/Users/Deepi/health_surveillance_app/lib/l10n'

langs = {
  'en': en_additions,
  'hi': hi_translations,
  'ta': ta_translations,
  'kn': kn_translations
}

for lang, additions in langs.items():
    file_path = os.path.join(l10n_dir, f'app_{lang}.arb')
    data = load_json(file_path)
    
    # Just update data with additions, but be careful with metadata (keys starting with @)
    # We'll just update directly
    for k, v in additions.items():
        data[k] = v
        
    save_json(file_path, data)

print("Updated arb files.")
