import wikipedia

from googletrans import Translator

from langcodes import *

#import iso_language_codes


def trans(text, des="en", od=1):
    translator = Translator()

    t = translator.translate(text=text, dest=des, src="auto")

    src = str(t.src)

    o_text = ol = oal = ""

    ol = Language.make(language=src).display_name()
    oal = Language.get(src).autonym()

    te = "<b>Translation</b> -\n\n"
    o_lang = "Original language : <b>" + ol + "</b>" + \
        " (<b>" + src + "</b>)" + " (<i>" + oal + "</i>)" + "\n"

    if od == 1:
        o_text = "Original text  : \n\n<i><code>" + text + \
            "</code></i>\n\n_____________________________________\n"

    dst = str(t.dest)
    ol = Language.make(language=dst).display_name()
    oal = Language.get(dst).autonym()
    tex = str(t.text)

    trans_to = "Translated To    :  <b>" + ol + "</b>" + \
        " (<b>" + dst + "</b>)" + " (<i>" + oal + "</i>)" + "\n"
    trans_text = "Translated text  : \n\n<i><code>" + tex + "</code></i>\n"

    gap = "\n"

    pren = ""

    p = str(t.pronunciation)

    if p != "None":
        if p != tex:
            pren = "\n_____________________________________\n\nPronunciation : <i>" + p + "</i>"

    ttt = te + o_lang + o_text + gap + trans_to + trans_text + pren

    return ttt


def search(query=None, urll=0):
    page = None
    text = title = content = url = ""
    try:
        page = wikipedia.page(query)
    except:
        text = "Search not found !"
        return text
    try:
        title = "Title : " + page.title + "\n\n"
    except:
        pass
    try:
        content = page.summary + "\n\n"
    except:
        pass
    try:
        if urll != 0:
            url = page.url
    except:
        pass

    text = title + content + url
    return text


def main():
    trans()


if __name__ == '__main__':
    main()


"""import googletrans
from google_images_search import GoogleImagesSearch


def trans():
    translator = Translator()
    #translator.translate('안녕하세요.')translator.translate('안녕하세요.')
    pass"""
