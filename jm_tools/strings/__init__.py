import re
from html.parser import HTMLParser


def camel_to_snake(my_string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', my_string).lower().replace("-", "_").replace(" ", "")


def is_zip_code(input_str):
    pattern = r"^\d{5}$"
    return bool(re.match(pattern, input_str))


def strip_html(text):
    output = ""

    def handle_data(data):
        nonlocal output
        output += data

    def handle_starttag(tag, attrs):
        nonlocal output
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    output += f" (link - {attr[1]})"
                    break

    def handle_endtag(tag):
        pass

    parser = HTMLParser()
    parser.handle_data = handle_data
    parser.handle_starttag = handle_starttag
    parser.handle_endtag = handle_endtag
    parser.feed(text)

    return output.strip()


def remove_words_starting_with_at_symbol(input_string):
    return re.sub(r'\@\w+', '', input_string)

def contains_chinese_characters(input_string):
    if re.search(r'[\u4e00-\u9fff]+', input_string):
        return True
    else:
        return False