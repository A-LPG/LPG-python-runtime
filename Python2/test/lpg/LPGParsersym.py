class LPGParsersym(object):
   TK_EQUIVALENCE   = 5
   TK_PRIORITY_EQUIVALENCE   = 6
   TK_ARROW   = 7
   TK_PRIORITY_ARROW   = 8
   TK_OR_MARKER   = 14
   TK_EQUAL   = 38
   TK_COMMA   = 37
   TK_LEFT_PAREN   = 39
   TK_RIGHT_PAREN   = 40
   TK_LEFT_BRACKET   = 42
   TK_RIGHT_BRACKET   = 43
   TK_SHARP   = 44
   TK_ALIAS_KEY   = 15
   TK_AST_KEY   = 16
   TK_DEFINE_KEY   = 17
   TK_DISJOINTPREDECESSORSETS_KEY   = 18
   TK_DROPRULES_KEY   = 19
   TK_DROPSYMBOLS_KEY   = 20
   TK_EMPTY_KEY   = 12
   TK_END_KEY   = 3
   TK_ERROR_KEY   = 9
   TK_EOL_KEY   = 10
   TK_EOF_KEY   = 13
   TK_EXPORT_KEY   = 21
   TK_GLOBALS_KEY   = 22
   TK_HEADERS_KEY   = 23
   TK_IDENTIFIER_KEY   = 11
   TK_IMPORT_KEY   = 24
   TK_INCLUDE_KEY   = 25
   TK_KEYWORDS_KEY   = 26
   TK_NAMES_KEY   = 27
   TK_NOTICE_KEY   = 28
   TK_OPTIONS_KEY   = 41
   TK_RECOVER_KEY   = 29
   TK_RULES_KEY   = 30
   TK_SOFT_KEYWORDS_KEY   = 31
   TK_START_KEY   = 32
   TK_TERMINALS_KEY   = 33
   TK_TRAILERS_KEY   = 34
   TK_TYPES_KEY   = 35
   TK_EOF_TOKEN   = 36
   TK_SINGLE_LINE_COMMENT   = 45
   TK_MACRO_NAME   = 2
   TK_SYMBOL   = 1
   TK_BLOCK   = 4
   TK_VBAR   = 46
   TK_ERROR_TOKEN   = 47

   orderedTerminalSymbols = [
                 "",
                 "SYMBOL",
                 "MACRO_NAME",
                 "END_KEY",
                 "BLOCK",
                 "EQUIVALENCE",
                 "PRIORITY_EQUIVALENCE",
                 "ARROW",
                 "PRIORITY_ARROW",
                 "ERROR_KEY",
                 "EOL_KEY",
                 "IDENTIFIER_KEY",
                 "EMPTY_KEY",
                 "EOF_KEY",
                 "OR_MARKER",
                 "ALIAS_KEY",
                 "AST_KEY",
                 "DEFINE_KEY",
                 "DISJOINTPREDECESSORSETS_KEY",
                 "DROPRULES_KEY",
                 "DROPSYMBOLS_KEY",
                 "EXPORT_KEY",
                 "GLOBALS_KEY",
                 "HEADERS_KEY",
                 "IMPORT_KEY",
                 "INCLUDE_KEY",
                 "KEYWORDS_KEY",
                 "NAMES_KEY",
                 "NOTICE_KEY",
                 "RECOVER_KEY",
                 "RULES_KEY",
                 "SOFT_KEYWORDS_KEY",
                 "START_KEY",
                 "TERMINALS_KEY",
                 "TRAILERS_KEY",
                 "TYPES_KEY",
                 "EOF_TOKEN",
                 "COMMA",
                 "EQUAL",
                 "LEFT_PAREN",
                 "RIGHT_PAREN",
                 "OPTIONS_KEY",
                 "LEFT_BRACKET",
                 "RIGHT_BRACKET",
                 "SHARP",
                 "SINGLE_LINE_COMMENT",
                 "VBAR",
                 "ERROR_TOKEN"
             ]

   numTokenKinds   = 47
   isValidForParser  = True

