digit_map = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩","01234567890123456789")

class ToEnglishDigits:
    def to_english_digits(text):
        return text.translate(digit_map)