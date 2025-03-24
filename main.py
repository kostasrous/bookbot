from stats import word_counter
from stats import symbol_counter
from stats import report
import sys
if len(sys.argv) < 2 :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path,"rt",encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents
def main():
    file = str(sys.argv[1])
    #file = "books/frankenstein.txt"
    counter = symbol_counter(get_book_text(file))
    the_report = report(counter)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------\nFound {word_counter(get_book_text(file))} total words")
    print("--------- Character Count -------")
    for i in range(len(the_report)):
        key = the_report[i]["name"]
        #print(key.isalpha())
        if key.isalpha():
            print(f"{key}:",the_report[i]["count"])
        else: continue
    print("============= END ===============")
main()