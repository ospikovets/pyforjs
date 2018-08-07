import enum

from .exceptions import LexerException


class TokenType(enum.Enum):
    """Available types of token"""

    String = 'string'


class Token:
    """An object describing the lexeme.

    A lexeme is a single identifiable sequence of characters.
    """

    def __init__(self, type: TokenType, value: str, line: int, column: int):
        """Token constructor.

        :param type: A TokenType corresponding to the type of newly created token.
        :type type: TokenType

        :param value: The string value of the token.
        :type value: str

        :param line: The line number where the token was encountered in the source code.
        :type line: int

        :param column: The column number where the token was encountered in the source code.
        :type column: int
        """

        self.type = type
        self.value = value
        self.line = line
        self.column = column


class Lexer:
    """An object that describes a lexer.

    Lexer is a program that breaks down the input source code into a sequence of lexemes."""

    def __init__(self, input: str):
        """Lexer constructor.

        :param input: An input string that should be parsed into Tokens.
        :type input: str
        """
        self.input = input

    def next_token(self) -> Token:
        """Get next parsed token from the input.

        :return: Next parsed token from the input.
        :rtype: Token

        :raise: LexerException if token is invalid.
        """
