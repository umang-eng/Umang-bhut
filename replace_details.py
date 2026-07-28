import os

replacements = {
    "Sharann Manojkumar": "Umang Bhut",
    "SHARANN MANOJKUMAR": "UMANG BHUT",
    "Sharann-del": "UmangBhut",
    "Sharann": "Umang",
    "sharann": "umangbhut",
    "sharannmanojkumar@gmail.com": "umangbhut10@gmail.com",
    "Chennai, India": "Ahmedabad, India",
    "CHENNAI, IN": "AHMEDABAD, IN",
    "Chennai, IN": "Ahmedabad, IN",
    "Chennai": "Ahmedabad",
    "13.08° N": "23.02° N",
    "VIT": "IITE",
    "Vellore Institute of Technology": "Indus Institute of Technology & Engineering",
    "2024 / 2028": "2023 / 2027",
    "3RD-YEAR CS @ VIT CHENNAI": "FINAL-YEAR IT @ IITE AHMEDABAD",
    "third-year CS student at Vellore Institute of Technology, Chennai.": "final-year IT student at Indus Institute of Technology & Engineering, Ahmedabad.",
    "iOS & Full-Stack Developer": "AI / ML Engineer",
    "iOS & FULL-STACK DEVELOPER": "AI / ML ENGINEER",
    "iOS": "AI/ML",
    "IOS": "AI/ML",
    "SWIFT": "PYTHON",
    "SWIFTUI": "PYTORCH",
    "WIDGETKIT": "TENSORFLOW",
    "NOTION API": "SCIKIT-LEARN",
    "CORE DATA": "PANDAS"
}

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for k, v in replacements.items():
            content = content.replace(k, v)
            
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    directory = "/Users/umang/Downloads/Sharann-del-main"
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.svg') or file.endswith('.md'):
                process_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
