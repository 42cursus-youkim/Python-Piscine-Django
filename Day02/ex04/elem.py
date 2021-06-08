#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        replace_list = [
            ["<", "&lt;"],
            [">", "&gt;"],
            ['"', "&quot;"],
            ["\n", "\n<br />\n"],
        ]
        result = super().__str__()
        for r in replace_list:
            result = result.replace(r[0], r[1])
        return result
        # return super().__str__().replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """

    # [...]
    class ValidationError(Exception):
        def __init__(self, msg="Content either not a _Text_ or _Elem_"):
            Exception.__init__(self, msg)

    def __init__(
        self, tag="div", attr={}, content: list = None, tag_type="double"
    ):
        """
        __init__() method.

        Obviously.
        """
        # [...]
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type
        self.content: list = list()
        if content:
            self.add_content(content)
        elif content is not None:
            if not isinstance(content, Text):
                raise Elem.ValidationError

        # self.mode = mode

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """

        result = [
            "<" + self.tag + self.__make_attr() + ">",
            self.__make_content(),
        ]
        if self.tag_type == "double":
            result.append("</" + self.tag + ">")
        elif self.tag_type == "simple":
            pass
        return "".join(map(str, result))

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ""
        for pair in sorted(self.attr.items()):
            result += " " + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        # print("my first is:", type(self.content[0]))
        tab = " " * 2
        if len(self.content) == 0:
            return ""
        # if (
        #     self.mode == "one"
        #     and len(self.content) == 1
        #     and type(self.content[0]) is Text
        # ):
        #     return "".join(self.content)
        result = "\n"
        for elem in self.content:
            new = str(elem).replace("\n", "\n" + tab)
            result += tab + new + "\n"
            # result += [...]
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text("")]
        elif content != Text(""):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (
            isinstance(content, Elem)
            or type(content) == Text
            or (
                type(content) == list
                and all(
                    [
                        type(elem) == Text or isinstance(elem, Elem)
                        for elem in content
                    ]
                )
            )
        )


if __name__ == "__main__":
    elem = Elem(
        tag="html",
        content=[
            Elem(
                tag="head",
                content=[Elem(tag="title", content=Text('"Hello ground!"'))],
            ),
            Elem(
                tag="body",
                content=[
                    Elem(tag="h1", content=Text('"Oh no, not again!"')),
                    Elem(
                        tag="img",
                        attr={"src": "http://i.imgur.com/pfp3T.jpg"},
                        tag_type="simple",
                    ),
                ],
            ),
        ],
    )
    print(elem)
