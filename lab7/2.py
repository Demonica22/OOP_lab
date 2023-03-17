class Utils:
    def reverse(self, s: list[str]) -> None:
        """
        Reverses the given list of strings, changing the given values
        :param s:
        :return: None
        """
        for i in range(len(s)):
            string = s[i]
            temp_str = ""
            for j in range(len(string) - 1, -1, -1):
                temp_str += string[j]
            s[i] = temp_str


u = Utils()
message = input("Enter string to be reversed: \n")
strings = [message]
u.reverse(strings)
print(strings[0])
