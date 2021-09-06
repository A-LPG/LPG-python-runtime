class LPGParsersym(object):
   TK_EQUIVALENCE : int  = 5
   TK_PRIORITY_EQUIVALENCE : int  = 6
   TK_ARROW : int  = 7
   TK_PRIORITY_ARROW : int  = 8
   TK_OR_MARKER : int  = 14
   TK_EQUAL : int  = 38
   TK_COMMA : int  = 37
   TK_LEFT_PAREN : int  = 39
   TK_RIGHT_PAREN : int  = 40
   TK_LEFT_BRACKET : int  = 42
   TK_RIGHT_BRACKET : int  = 43
   TK_SHARP : int  = 44
   TK_ALIAS_KEY : int  = 15
   TK_AST_KEY : int  = 16
   TK_DEFINE_KEY : int  = 17
   TK_DISJOINTPREDECESSORSETS_KEY : int  = 18
   TK_DROPRULES_KEY : int  = 19
   TK_DROPSYMBOLS_KEY : int  = 20
   TK_EMPTY_KEY : int  = 12
   TK_END_KEY : int  = 3
   TK_ERROR_KEY : int  = 9
   TK_EOL_KEY : int  = 10
   TK_EOF_KEY : int  = 13
   TK_EXPORT_KEY : int  = 21
   TK_GLOBALS_KEY : int  = 22
   TK_HEADERS_KEY : int  = 23
   TK_IDENTIFIER_KEY : int  = 11
   TK_IMPORT_KEY : int  = 24
   TK_INCLUDE_KEY : int  = 25
   TK_KEYWORDS_KEY : int  = 26
   TK_NAMES_KEY : int  = 27
   TK_NOTICE_KEY : int  = 28
   TK_OPTIONS_KEY : int  = 41
   TK_RECOVER_KEY : int  = 29
   TK_RULES_KEY : int  = 30
   TK_SOFT_KEYWORDS_KEY : int  = 31
   TK_START_KEY : int  = 32
   TK_TERMINALS_KEY : int  = 33
   TK_TRAILERS_KEY : int  = 34
   TK_TYPES_KEY : int  = 35
   TK_EOF_TOKEN : int  = 36
   TK_SINGLE_LINE_COMMENT : int  = 45
   TK_MACRO_NAME : int  = 2
   TK_SYMBOL : int  = 1
   TK_BLOCK : int  = 4
   TK_VBAR : int  = 46
   TK_ERROR_TOKEN : int  = 47

   orderedTerminalSymbols : list= [
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

   numTokenKinds : int  = 47
   isValidForParser : bool = True

