class Cipher:
    def __init__(
        self,
        text: str,
        code1: int,
        code2: int,
        code3: int,
        blug_panel=False,
        blugs={
            "a": False,
            "b": False,
            "c": False,
            "d": False,
            "e": False,
            "f": False,
            "g": False,
            "h": False,
            "i": False,
            "j": False,
            "k": False,
            "l": False,
            "m": False,
        },
    ) -> None:
        self.input = text
        self.first = code1
        self.second = code2
        self.third = code3
        self.blug_panel = blug_panel
        self.blugs = blugs
        self.order = self.get_keyboard()
        self.original_order = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            " ",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            ".",
            ",",
            "/",
            "\\",
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "(",
            "*",
            ")",
            "_",
            "-",
            "=",
            "+",
            "|",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
            "[",
            "]",
            "{",
            "}",
        ]
        self.original_mirror = self.list2dict()
        self.original = self.list2dict()
        self.order1 = self.randomize_order(self.order, self.original, code1)
        self.order2 = self.randomize_order(self.order, self.order1, code2)
        self.order3 = self.randomize_order(self.order, self.order2, code3)
        self.output = self.encode()

    def get_keyboard(self):
        new = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            " ",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            ".",
            ",",
            "/",
            "\\",
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "(",
            "*",
            ")",
            "_",
            "-",
            "=",
            "+",
            "|",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
            "[",
            "]",
            "{",
            "}",
        ]
        return new

    def list2dict(self):
        new = {}
        for i in self.order:
            new[i] = i
        return new

    def randomize_order(self, order: list, original: dict, code: int):
        new = {}
        n = code
        original = list(original.values())
        while len(order) > 0:
            for i in order:
                index = order.index(i) + n
                while index >= len(order):
                    index = index - len(order)
                j = original[index]
                new[i] = j
                new[j] = i
                order.remove(i)
                original.remove(j)
                if i != j:
                    order.remove(j)
                    original.remove(i)
                n += 1
                if n >= len(order):
                    n = 0

        self.order = self.get_keyboard()
        # print(new)
        return new

    def encode(self):
        paragraph = ""
        if not self.blug_panel:
            for letter in self.input:
                paragraph += self.order3[letter]

        return paragraph


eng = Cipher("qre(5+OpWeBK", 500, 1000, 20000)
print(eng.output)
