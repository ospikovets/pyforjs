import enum
from typing import (
    Callable,
    NewType,
    Set,
    Text,
)

from .exceptions import LexerException

State = NewType('State', int)


class TokenType(enum.Enum):
    """Enum of available token types."""

    String = 'string'


class Token:
    """Class that describes a Lexeme.

    A lexeme is a single identifiable sequence of characters.
    """

    def __init__(self, type: TokenType, value: Text, line: int, column: int) -> None:
        """Token constructor.

        :param type: A TokenType corresponding to the type of newly created token.
        :type type: TokenType

        :param value: The string value of the token.
        :type value: Text

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
    """Class that describes a Lexical Analyzer.

    Lexer is a program that breaks down the input source code into a sequence of lexemes."""

    def __init__(self, input: Text) -> None:
        """Lexer constructor.

        :param input: An input string that should be parsed into Tokens.
        :type input: Text
        """
        self.input = input

    def next_token(self) -> Token:
        """Get next parsed token from the input.

        :return: Next parsed token from the input.
        :rtype: Token

        :raise: LexerException if token is invalid.
        """


class FSM:
    """Class that describes Finite State Machine."""

    def __init__(self,
                 states: Set[State],
                 initial_state: State,
                 accepting_states: Set[State],
                 next_state: Callable[[State, Text], State]) -> None:
        """FSM constructor.

        :param states:
        :type states: Set[State]

        :param initial_state: The state FSM starts execution from.
        :type initial_state: State

        :param accepting_states: A subset of all possible FSM states
        that are accepted as the FSM exit points.
        :type accepting_states: Set[State]

        :param next_state: Function that describes the transition
        from the current state to the next state.
        :type next_state: Callable[[State, Text], State]
        """

        self.states = states
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.next_state = next_state

    def run(self, input: Text) -> bool:
        """Check if 'input' or a subset of 'input' matches regular expression.

        :param input: Text to process though the FSM.
        :type input: Text

        :return: True if 'input' or a subset of 'input' matches
        the regular expression corresponding to this FSM.
        :rtype: bool
        """

        current_state = self.initial_state

        for char in input:
            next_state = self.next_state(current_state, char)

            if next_state in self.accepting_states:
                return True
            elif next_state not in self.states:
                break

            current_state = next_state

        return current_state in self.accepting_states
