import re


class Punctuation:
    def comma_correction(self, x):
        """
            remove extra spaces before and after comma ( , )
            """
        self.x = x
        return re.sub(re.compile(r"\u0020,\u0020|\u0020,|,\u0020"), r", ", x)

    def point_correction(self, x):
        """
            remove extra spaces before and after point ( . )
            """
        self.x = x
        return re.sub(re.compile(r"\u0020\.\u0020|\u0020\.|\.\u0020"), r". ", x)

    def semicolon_correction(self, x):
        """
            remove extra spaces before and after semicolon ( ; )
            """
        self.x = x
        return re.sub(re.compile(r"\u0020;\u0020|\u0020;|;\u0020"), r"; ", x)

    def colon_correction(self, x):
        """
            remove extra spaces before and after colon ( : )
            """
        self.x = x
        return re.sub(re.compile(r"\u0020:\u0020|\u0020:|:\u0020"), r": ", x)

    def questionmark_correction(self, x):
        """
            remove extra spaces before and after question mark ( ? )
            """
        self.x = x
        return re.sub(re.compile(r"\u0020\?\u0020|\u0020\?|\?\u0020"), r"? ", x)

    def exclamationmark_correction(self, x):
        """
            remove extra spaces before and after exclamation mark ( ! )
            """
        self.x = x
        return re.sub(re.compile(r"\u0020!\u0020|\u0020!|!\u0020"), r"! ", x)

    def puncsIssues(self, content):
        """
            Checking all the punctuation issues related to latin-based Kurdish text
            """
        self.content = content
        all_funcs = (
            Punctuation().comma_correction,
            Punctuation().point_correction,
            Punctuation().semicolon_correction,
            Punctuation().colon_correction,
            Punctuation().questionmark_correction,
            Punctuation().exclamationmark_correction,
        )

        for func in all_funcs:
            content = func(content)

        return content
