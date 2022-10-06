class ColorizePrint:
    colors = {
        'PURPLE': "\033[95m",
        'BLUE': "\033[94m",
        'GREEN': "\033[92m",
        'RED': "\033[91m",
        'YELLOW': "\033[93m",
        'CYAN': "\033[96m",
    }
    others = {
        'BOLD': "\033[1m",
        'UNDERLINE': "\033[4m",
        'END': "\033[0m"
    }


    @classmethod
    def colorizeDefault(cls, string, bold=False, underline=False):
        return cls.colorize("", string, bold, underline)

    @classmethod
    def colorizeHeader(cls, string, bold=False, underline=False):
        return cls.colorize(cls.colors["PURPLE"], string, bold, underline)

    @classmethod
    def colorizePrimary(cls, string, bold=False, underline=False):
        return cls.colorize(cls.colors["BLUE"], string, bold, underline)

    @classmethod
    def colorizeSuccess(cls, string, bold=False, underline=False):
        return cls.colorize(cls.colors["GREEN"], string, bold, underline)

    @classmethod
    def colorizeError(cls, string, bold=False, underline=False):
        return cls.colorize(cls.colors["RED"], string, bold, underline)

    @classmethod
    def colorizeWarning(cls, string, bold=False, underline=False):
        return cls.colorize(cls.colors["YELLOW"], string, bold, underline)

    @classmethod
    def colorizeInfo(cls, string, bold=False, underline=False):
        return cls.colorize(cls.colors["CYAN"], string, bold, underline)

    @classmethod
    def colorize(cls, color, string, bold=False, underline=False) -> str:
        # BOLD
        color = color + cls.others["BOLD"] if bold else color
        # UNDERLINE
        color = color + cls.others["UNDERLINE"] if underline else color
        # END
        end = cls.others["END"] if color else ""

        return f"{color}{string}{end}"


def test_colorize():
    print(ColorizePrint.colorizeDefault("TEST"))
    print(ColorizePrint.colorizeHeader("TEST"))
    print(ColorizePrint.colorizePrimary("TEST"))
    print(ColorizePrint.colorizeSuccess("TEST"))
    print(ColorizePrint.colorizeError("TEST"))
    print(ColorizePrint.colorizeWarning("TEST"))
    print(ColorizePrint.colorizeInfo("TEST"))
    print(ColorizePrint.colorizeInfo("TEST", bold=True))
    print(ColorizePrint.colorizeInfo("TEST", bold=True, underline=True))
    print(ColorizePrint.colorizeDefault("TEST", bold=True))
    print(ColorizePrint.colorizeDefault("TEST", bold=True, underline=True))


if __name__ == "__main__":
    test_colorize()
