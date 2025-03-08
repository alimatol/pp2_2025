path = r"C:\Users\user\Documents\Challenging situation in the past.txt"
def count_lines(file):
    with open(file, 'r', encoding='utf-8-sig', errors='ignore' ) as text:
        return len(text.readlines())

line_count = count_lines(path)
print(f"Amount of lines: {line_count}")
