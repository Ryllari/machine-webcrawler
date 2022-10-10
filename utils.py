import re

def remove_tabs_and_new_lines_from_text(text):
    return text.replace("\n", "").replace("\t", "")

def remove_b_tags(text):
    return text.replace("<b>", "").replace("</b>", "")

def get_b_content(text):
    if "<b>" in text:
        return re.findall(r"<b>(.*)</b>", text)[0]
    return text