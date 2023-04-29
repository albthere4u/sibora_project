import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def read_break_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        break_words = [line.strip() for line in file]
    return break_words

def clean_text(text, line_break_words):
    cleaned_text = ' '.join(text.split())
    for word in line_break_words:
        cleaned_text = cleaned_text.replace(word, f"\n{word}")
    return cleaned_text

if __name__ == "__main__":
    pdf_path = "/Users/seokdaegeon/PycharmProjects/sibora/seoulsibo_20230426151204_73863.pdf"  # 여기에 PDF 파일 경로를 입력하세요.
    extracted_text = extract_text_from_pdf(pdf_path)

    break_word_file = "break_words.txt"
    line_break_words = read_break_words_from_file(break_word_file)
    cleaned_text = clean_text(extracted_text, line_break_words)

    truncated_text = cleaned_text[:30000]
    print(truncated_text)
