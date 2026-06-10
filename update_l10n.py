import json
import os

l10n_dir = 'c:/Users/Deepi/health_surveillance_app/lib/l10n'
files = {
    'app_en.arb': {
        "mobileNumber": "Mobile Number",
        "enterMobileNumber": "Enter valid mobile number",
        "smsSentToMobile": "SMS Alert sent to {mobile}"
    },
    'app_kn.arb': {
        "mobileNumber": "ಮೊಬೈಲ್ ಸಂಖ್ಯೆ",
        "enterMobileNumber": "ಮಾನ್ಯವಾದ 10 ಅಂಕಿಯ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ",
        "smsSentToMobile": "SMS ಎಚ್ಚರಿಕೆಯನ್ನು {mobile} ಗೆ ಕಳುಹಿಸಲಾಗಿದೆ"
    },
    'app_hi.arb': {
        "mobileNumber": "मोबाइल नंबर",
        "enterMobileNumber": "वैध 10 अंकों का मोबाइल नंबर दर्ज करें",
        "smsSentToMobile": "SMS अलर्ट {mobile} पर भेजा गया"
    },
    'app_ta.arb': {
        "mobileNumber": "மொபைல் எண்",
        "enterMobileNumber": "சரியான 10 இலக்க மொபைல் எண்ணை உள்ளிடவும்",
        "smsSentToMobile": "SMS எச்சரிக்கை {mobile} க்கு அனுப்பப்பட்டது"
    }
}

for fname, new_keys in files.items():
    path = os.path.join(l10n_dir, fname)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for k, v in new_keys.items():
            data[k] = v
        
        # if smsSentToMobile needs a placeholder, Flutter l10n expects the @key entry too
        if "smsSentToMobile" in new_keys:
            data["@smsSentToMobile"] = {
                "placeholders": {
                    "mobile": {
                        "type": "String"
                    }
                }
            }

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Updated {fname}")
