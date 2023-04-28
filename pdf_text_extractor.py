
def read_break_word_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        break_word = file.read().strip()
    return break_word

if __name__ == "__main__":
    pdf_path = "/Users/seokdaegeon/PycharmProjects/sibora/seoulsibo_20230426151204_73863.pdf"  # 여기에 PDF 파일 경로를 입력하세요.
    extracted_text = extract_text_from_pdf(pdf_path)

    break_word_file = "break_words.txt"
    line_break_word = read_break_word_from_file(break_word_file)
    cleaned_text = clean_text(extracted_text, line_break_word)

    truncated_text = cleaned_text[:3000]
    print(truncated_text)
