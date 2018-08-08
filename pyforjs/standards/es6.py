"""ECMAScript2015 special symbols and reserved words.

This module defines ECMAScript2015 (ES6) special symbols and reserved words with the set of Enums.
"""

from enum import Enum


class ControlCharacters(Enum):
    """ECMAScript2015 control characters.

    Enum of control characters according to:
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar
    """

    ZWNJ = '\u200C'  # Zero width non-joiner
    ZWJ = '\u200D'  # Zero width joiner
    BOM = '\uFEFF'  # Byte order mark


class WhiteSpace(Enum):
    """ECMAScript2015 white space characters.

    Enum of white space characters according to:
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar
    """

    HT = '\u0009'  # Horizontal tabulation
    VT = '\u000B'  # Vertical tabulation
    FF = '\u000C'  # Form feed
    SP = '\u0020'  # Normal space
    NBSP = '\u00A0'  # No-break space


class LineTerminators(Enum):
    """ECMAScript2015 line terminator characters.

    Enum of line terminator characters according to:
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar
    """

    LF = '\u000A'  # Line feed
    CR = '\u000D'  # Carriage return
    LS = '\u2028'  # Line separator
    PS = '\u2029'  # Paragraph separator


class Comments(Enum):
    """ECMAScript2015 comments."""

    SINGLE_LINE = '//'
    MULTI_LINE_START = '/*'
    MULTI_LINE_END = '*/'


class ReservedKeywords(Enum):
    """ECMAScript2015 reserved keywords.

    Enum of reserved keywords in ECMAScript2015 according to:
    https://developer.mozilla.org/docs/Web/JavaScript/Reference/Lexical_grammar
    """

    BREAK = 'break'
    CASE = 'case'
    CATCH = 'catch'
    CLASS = 'class'
    CONST = 'const'
    CONTINUE = 'continue'
    DEBUGGER = 'debugger'
    DEFAULT = 'default'
    DELETE = 'delete'
    DO = 'do'
    ELSE = 'else'
    EXPORT = 'export'
    EXTENDS = 'extends'
    FINALLY = 'finally'
    FOR = 'for'
    FUNCTION = 'function'
    IF = 'if'
    IMPORT = 'import'
    IN = 'in'
    INSTANCEOF = 'instanceof'
    NEW = 'new'
    RETURN = 'return'
    SUPER = 'super'
    SWITCH = 'switch'
    THIS = 'this'
    THROW = 'throw'
    TRY = 'try'
    TYPEOF = 'typeof'
    VAR = 'var'
    VOID = 'void'
    WHILE = 'while'
    WITH = 'with'
    YIELD = 'yield'


class FutureReservedKeywords(Enum):
    """ECMAScript2015 future reserved keywords.

    Enum of future reserved keywords in ECMAScript2015 according to:
    https://developer.mozilla.org/docs/Web/JavaScript/Reference/Lexical_grammar
    """

    # Always reserved
    ENUM = 'enum'

    # Reserved only in "strict mode"
    IMPLEMENTS = 'implements'
    INTERFACE = 'interface'
    LET = 'let'
    PACKAGE = 'package'
    PRIVATE = 'private'
    PROTECTED = 'protected'
    PUBLIC = 'public'
    STATIC = 'static'

    # Reserved only in module code
    AWAIT = 'await'


class FutureReservedKeywordsInOlderStandards(Enum):
    """Older ECMAScript2015 reserved keywords.

    The following are reserved as future keywords by older
    ECMAScript specifications (ECMAScript 1 till 3) according to:
    https://developer.mozilla.org/docs/Web/JavaScript/Reference/Lexical_grammar
    """

    ABSTRACT = 'abstract'
    BOOLEAN = 'boolean'
    BYTE = 'byte'
    CHAR = 'char'
    DOUBLE = 'double'
    FINAL = 'final'
    FLOAT = 'float'
    GOTO = 'goto'
    INT = 'int'
    LONG = 'long'
    NATIVE = 'native'
    SHORT = 'short'
    SYNCHRONIZED = 'synchronized'
    THROWS = 'throws'
    TRANSIENT = 'transient'
    VOLATILE = 'volatile'


class LiteralWords(Enum):
    """ECMAScript2015 reserved words for literals.

    Enum of reserved words that are literals according to:
    https://developer.mozilla.org/docs/Web/JavaScript/Reference/Lexical_grammar
    """

    NULL = 'null'
    TRUE = 'true'
    FALSE = 'false'
