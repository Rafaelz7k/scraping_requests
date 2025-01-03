from unidecode import unidecode

def remove_accent(text):
    return unidecode(text)

def get_title(title_tag):
    try:
        title = title_tag['title']
    except (TypeError, KeyError):
        title = ""

    try:
        title = title_tag.get_text(strip=True)
    except Exception:
        title = title_tag.text.strip()

    return title

def get_float(price):
    if price:
        text = price.get_text(strip=True)
        cleaned_text = text.replace('R$', '').replace('.', '').replace(',', '.')

        return float(cleaned_text) if cleaned_text else 0.0
    return 0.0
