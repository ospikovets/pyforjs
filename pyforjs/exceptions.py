class AnalyzerException(Exception):
    """Base exception class for the package."""


class LexerException(AnalyzerException):
    """Lexical Analyzer exception.

    Raised when Lexer is unable to parse input string into tokens.
    """
