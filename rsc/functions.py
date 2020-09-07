class translator():
    
    def __init__(self, text):
        self.text = text
    
    def translate_cyrillyc(text):
        symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                   u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")
        tr = {ord(a):ord(b) for a, b in zip(*symbols)}
        return text.translate(tr)
    
    def change_format(date):
        pattern = r'(\d{4})-(\d{2})-(\d{2})'
        return re.sub(pattern, '\\1', date)

