#!/usr/bin/python3

from elem import Text, Elem


class Html(Elem):
    tag = "html"

    def __init__(self, _content=None):
        super().__init__(tag=self.tag, content=_content)


class Div(Html):
    tag = "div"


class Span(Html):
    tag = "span"


class Head(Html):
    tag = "head"


class Body(Html):
    tag = "body"


class Title(Elem):
    tag = "title"

    def __init__(self, text=None):
        if type(text) is str:
            super().__init__(tag=self.tag, content=Text(text))
        else:
            super().__init__(tag=self.tag, content=[Text(t) for t in text])


class H1(Title):
    tag = "h1"


class H2(Title):
    tag = "h2"


class P(Title):
    tag = "p"


class Meta(Elem):
    tag = "meta"

    def __init__(self, _attr={}):
        super().__init__(tag=self.tag, attr=_attr, tag_type="simple")


class Img(Meta):
    tag = "img"


class Table(Html):
    tag = "table"


class Tr(Table):
    tag = "tr"


class Th(Title):
    tag = "th"


class Td(Title):
    tag = "td"


class Ol(Table):
    tag = "ol"


class Ul(Table):
    tag = "ul"


class Li(Title):
    tag = "li"


class Hr(Html):
    pass


class Br(Meta):
    tag = "br"

    def __init__(self):
        super().__init__(tag=self.tag, attr={}, tag_type="simple")


if __name__ == "__main__":

    html1 = Html(
        [
            Head([Meta({"char": "utf-8"})]),
            Body([Table()]),
        ]
    )
    html2 = Html(
        [
            P("Apollo"),
            Title("Hello"),
            Ul(
                [
                    Li("Neil"),
                    Li("Buzz"),
                ]
            ),
        ]
    )
    htmlmaster = Html(
        [
            Head([Title("Hello Ground!")]),
            Body(
                [
                    H1("Oh no, not again!"),
                    Img({"src": "http://i.imgur.com/pfp3T.jpg"}),
                    P(["Hi", "some multiline", "paragraph"]),
                ]
            ),
        ]
    )
    print(htmlmaster)
