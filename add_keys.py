import json
import os

l10n_dir = 'c:/Users/Deepi/health_surveillance_app/lib/l10n'
files = {
    'app_en.arb': {
        "totalReports": "Total Reports",
        "homeTab": "Home",
        "menuTab": "Menu"
    },
    'app_kn.arb': {
        "totalReports": "ಒಟ್ಟು ವರದಿಗಳು",
        "homeTab": "ಮುಖಪುಟ",
        "menuTab": "ಮೆನು"
    },
    'app_hi.arb': {
        "totalReports": "कुल रिपोर्ट",
        "homeTab": "होम",
        "menuTab": "मेनू"
    },
    'app_ta.arb': {
        "totalReports": "மொத்த அறிக்கைகள்",
        "homeTab": "முகப்பு",
        "menuTab": "பட்டி"
    }
}

for fname, new_keys in files.items():
    path = os.path.join(l10n_dir, fname)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for k, v in new_keys.items():
            data[k] = v
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Updated {fname}")
