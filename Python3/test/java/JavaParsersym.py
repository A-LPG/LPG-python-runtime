#
# This is the grammar specification from the Final Draft of the generic spec.
#
########################################
# Copyright (c) 2007 IBM Corporation.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http:#www.eclipse.org/legal/epl-v10.html
#
#Contributors:
#    Philippe Charles (pcharles@us.ibm.com) - initial API and implementation

########################################

class JavaParsersym(object):
   TK_ClassBodyDeclarationsoptMarker : int  = 102
   TK_LPGUserActionMarker : int  = 103
   TK_IntegerLiteral : int  = 32
   TK_LongLiteral : int  = 33
   TK_FloatingPointLiteral : int  = 34
   TK_DoubleLiteral : int  = 35
   TK_CharacterLiteral : int  = 36
   TK_StringLiteral : int  = 37
   TK_MINUS_MINUS : int  = 26
   TK_OR : int  = 86
   TK_MINUS : int  = 46
   TK_MINUS_EQUAL : int  = 72
   TK_NOT : int  = 48
   TK_NOT_EQUAL : int  = 87
   TK_REMAINDER : int  = 88
   TK_REMAINDER_EQUAL : int  = 73
   TK_AND : int  = 68
   TK_AND_AND : int  = 89
   TK_AND_EQUAL : int  = 74
   TK_LPAREN : int  = 3
   TK_RPAREN : int  = 20
   TK_MULTIPLY : int  = 69
   TK_MULTIPLY_EQUAL : int  = 75
   TK_COMMA : int  = 43
   TK_DOT : int  = 42
   TK_DIVIDE : int  = 90
   TK_DIVIDE_EQUAL : int  = 76
   TK_COLON : int  = 50
   TK_SEMICOLON : int  = 4
   TK_QUESTION : int  = 91
   TK_AT : int  = 1
   TK_LBRACKET : int  = 23
   TK_RBRACKET : int  = 53
   TK_XOR : int  = 92
   TK_XOR_EQUAL : int  = 77
   TK_LBRACE : int  = 27
   TK_OR_OR : int  = 95
   TK_OR_EQUAL : int  = 78
   TK_RBRACE : int  = 45
   TK_TWIDDLE : int  = 49
   TK_PLUS : int  = 47
   TK_PLUS_PLUS : int  = 28
   TK_PLUS_EQUAL : int  = 79
   TK_LESS : int  = 24
   TK_LEFT_SHIFT : int  = 70
   TK_LEFT_SHIFT_EQUAL : int  = 80
   TK_LESS_EQUAL : int  = 81
   TK_EQUAL : int  = 51
   TK_EQUAL_EQUAL : int  = 93
   TK_GREATER : int  = 44
   TK_GREATER_EQUAL : int  = 112
   TK_RIGHT_SHIFT : int  = 113
   TK_RIGHT_SHIFT_EQUAL : int  = 114
   TK_UNSIGNED_RIGHT_SHIFT : int  = 115
   TK_UNSIGNED_RIGHT_SHIFT_EQUAL : int  = 116
   TK_ELLIPSIS : int  = 96
   TK_BeginAction : int  = 104
   TK_EndAction : int  = 105
   TK_BeginJava : int  = 106
   TK_EndJava : int  = 107
   TK_NoAction : int  = 108
   TK_NullAction : int  = 109
   TK_BadAction : int  = 110
   TK_abstract : int  = 17
   TK_assert : int  = 57
   TK_boolean : int  = 5
   TK_break : int  = 58
   TK_byte : int  = 6
   TK_case : int  = 71
   TK_catch : int  = 97
   TK_char : int  = 7
   TK_class : int  = 31
   TK_const : int  = 117
   TK_continue : int  = 59
   TK_default : int  = 67
   TK_do : int  = 60
   TK_double : int  = 8
   TK_enum : int  = 41
   TK_else : int  = 94
   TK_extends : int  = 82
   TK_false : int  = 38
   TK_final : int  = 19
   TK_finally : int  = 98
   TK_float : int  = 9
   TK_for : int  = 61
   TK_goto : int  = 118
   TK_if : int  = 62
   TK_implements : int  = 111
   TK_import : int  = 99
   TK_instanceof : int  = 83
   TK_int : int  = 10
   TK_interface : int  = 21
   TK_long : int  = 11
   TK_native : int  = 84
   TK_new : int  = 29
   TK_null : int  = 39
   TK_package : int  = 100
   TK_private : int  = 14
   TK_protected : int  = 15
   TK_public : int  = 12
   TK_return : int  = 63
   TK_short : int  = 13
   TK_static : int  = 16
   TK_strictfp : int  = 18
   TK_super : int  = 25
   TK_switch : int  = 64
   TK_synchronized : int  = 52
   TK_this : int  = 30
   TK_throw : int  = 65
   TK_throws : int  = 101
   TK_transient : int  = 54
   TK_true : int  = 40
   TK_try : int  = 66
   TK_void : int  = 22
   TK_volatile : int  = 55
   TK_while : int  = 56
   TK_EOF_TOKEN : int  = 85
   TK_IDENTIFIER : int  = 2
   TK_ERROR_TOKEN : int  = 119

   orderedTerminalSymbols : list= [
                 "",
                 "AT",
                 "IDENTIFIER",
                 "LPAREN",
                 "SEMICOLON",
                 "boolean",
                 "byte",
                 "char",
                 "double",
                 "float",
                 "int",
                 "long",
                 "public",
                 "short",
                 "private",
                 "protected",
                 "static",
                 "abstract",
                 "strictfp",
                 "final",
                 "RPAREN",
                 "interface",
                 "void",
                 "LBRACKET",
                 "LESS",
                 "super",
                 "MINUS_MINUS",
                 "LBRACE",
                 "PLUS_PLUS",
                 "new",
                 "this",
                 "class",
                 "IntegerLiteral",
                 "LongLiteral",
                 "FloatingPointLiteral",
                 "DoubleLiteral",
                 "CharacterLiteral",
                 "StringLiteral",
                 "false",
                 "null",
                 "true",
                 "enum",
                 "DOT",
                 "COMMA",
                 "GREATER",
                 "RBRACE",
                 "MINUS",
                 "PLUS",
                 "NOT",
                 "TWIDDLE",
                 "COLON",
                 "EQUAL",
                 "synchronized",
                 "RBRACKET",
                 "transient",
                 "volatile",
                 "while",
                 "assert",
                 "break",
                 "continue",
                 "do",
                 "for",
                 "if",
                 "return",
                 "switch",
                 "throw",
                 "try",
                 "default",
                 "AND",
                 "MULTIPLY",
                 "LEFT_SHIFT",
                 "case",
                 "MINUS_EQUAL",
                 "REMAINDER_EQUAL",
                 "AND_EQUAL",
                 "MULTIPLY_EQUAL",
                 "DIVIDE_EQUAL",
                 "XOR_EQUAL",
                 "OR_EQUAL",
                 "PLUS_EQUAL",
                 "LEFT_SHIFT_EQUAL",
                 "LESS_EQUAL",
                 "extends",
                 "instanceof",
                 "native",
                 "EOF_TOKEN",
                 "OR",
                 "NOT_EQUAL",
                 "REMAINDER",
                 "AND_AND",
                 "DIVIDE",
                 "QUESTION",
                 "XOR",
                 "EQUAL_EQUAL",
                 "else",
                 "OR_OR",
                 "ELLIPSIS",
                 "catch",
                 "finally",
                 "import",
                 "package",
                 "throws",
                 "ClassBodyDeclarationsoptMarker",
                 "LPGUserActionMarker",
                 "BeginAction",
                 "EndAction",
                 "BeginJava",
                 "EndJava",
                 "NoAction",
                 "NullAction",
                 "BadAction",
                 "implements",
                 "GREATER_EQUAL",
                 "RIGHT_SHIFT",
                 "RIGHT_SHIFT_EQUAL",
                 "UNSIGNED_RIGHT_SHIFT",
                 "UNSIGNED_RIGHT_SHIFT_EQUAL",
                 "const",
                 "goto",
                 "ERROR_TOKEN"
             ]

   numTokenKinds : int  = 119
   isValidForParser : bool = True

