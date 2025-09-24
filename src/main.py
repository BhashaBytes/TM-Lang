import subprocess

mapping = {
    "காட்டிடு": "print", "kaattidu": "print",
    "எடுத்து": "input", "eduthu": "input",
    "என்றால்": "if", "enraal": "if",
    "இல்லை_என்றால்": "elif", "illainraal": "elif",
    "இல்லை": "else", "illai": "else",
    "காக": "for", "kaga": "for",
    "போது": "while", "pothu": "while",
    "வரையிடு": "def", "varaiyidu": "def",
    "வகுப்பு": "class", "vaguppu": "class",
    "திருப்பிடு": "return", "thiruppidu": "return",
    "நிறுத்திடு": "break", "niruthidu": "break",
    "தொடரிடு": "continue", "thodaridu": "continue",
    "உள்ளிடு": "import", "ulkollu": "import",
    "இருந்து": "from", "irundhu": "from",
    "ஆக": "as", "aaga": "as",
    "உடன்": "with", "udan": "with",
    "முயற்சிடு": "try", "muyarchidu": "try",
    "தவிர": "except", "thavira": "except",
    "இறுதியில்": "finally", "iruthil": "finally",
    "உண்மை": "True", "unmai": "True",
    "பொய்": "False", "poi": "False",
    "ஒன்றுமில்லை": "None", "onrumillai": "None",
    "அல்லது": "or", "allatu": "or",
}

def translate(code: str) -> str:
    for tam, eng in mapping.items():
        code = code.replace(tam, eng)
    return code

def run_tmlang_file(filename="test.tm"):
    with open(filename, "r", encoding="utf-8") as f:
        tamil_code = f.read()
    python_code = translate(tamil_code)
    with open("temp.py", "w", encoding="utf-8") as f:
        f.write(python_code)
    subprocess.run(["python3", "temp.py"])

if __name__ == "__main__":
    run_tmlang_file()
