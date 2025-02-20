import random
import json

def load_names(filename):
    """Belirtilen dosyadan isimleri satır satır yükler ve bir liste olarak döndürür."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Hata: {filename} dosyası bulunamadı!")
        return []

def normalize(name):
    """Türkçe karakterleri Latin harflerine çevirerek normalleştirir."""
    replacements = str.maketrans(
        "çğıöşüÇĞİÖŞÜ", "cgiösuCGIOSU"
    )
    return name.translate(replacements)

def generate_username(first_names, last_names):
    """Farklı formatlarda rastgele bir kullanıcı adı üretir ve uzunluk kontrolü yaparak uygunsa döndürür."""
    while True:
        first_name = normalize(random.choice(first_names))
        last_name = normalize(random.choice(last_names))
        
        case_options = [
            f"{first_name}{last_name}{random.randint(0, 99):02d}",
            f"{last_name}{first_name}{random.randint(0, 9999):04d}",
            f"{first_name}{random.randint(0, 99):02d}",
            f"{last_name}{random.randint(0, 99):02d}",
            f"{first_name}{random.randint(1989, 2002)}",
            f"{last_name}{random.randint(1989, 2002)}",
            f"{first_name}_{last_name}",
            f"{first_name.capitalize()}.{last_name.capitalize()}{random.randint(10, 99)}",
            f"{first_name.capitalize()}{random.randint(100, 999)}{last_name.capitalize()}",
            f"{first_name.capitalize()}{random.choice(['X', 'Y', 'Z'])}{last_name.capitalize()}",
            f"{first_name.capitalize()}{random.choice(['_', '-', '.'])}{random.randint(1, 9999)}",
            f"{first_name.capitalize()}{last_name[:3].capitalize()}{random.randint(10, 99)}",
            f"{first_name[:3].capitalize()}{last_name.capitalize()}{random.randint(10, 99)}",
            f"{first_name.upper()}{random.randint(10, 99)}_{last_name.upper()}",
            f"{first_name.upper()}-{random.randint(1989, 2002)}-{last_name.upper()}"
        ]
        
        username = random.choice(case_options)
        
        if 8 <= len(username) <= 12:
            return username

def main():
    """Ana fonksiyon: İsimleri yükler, 1500 kullanıcı adı üretir ve dosyalara kaydeder."""
    first_names = load_names('firstname.txt')
    last_names = load_names('lastname.txt')
    
    if not first_names or not last_names:
        print("İsim listeleri yüklenemedi, işlem durduruluyor.")
        return
    
    usernames = [generate_username(first_names, last_names) for _ in range(880000)]
    
    with open('usernames.json', 'w', encoding='utf-8') as json_file:
        json.dump(usernames, json_file, ensure_ascii=False, indent=4)
    
    with open('usernames.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write('\n'.join(usernames))
    
    print("✔ Kullanıcı adları usernames.json ve usernames.txt dosyalarına kaydedildi!")

if __name__ == "__main__":
    main()
