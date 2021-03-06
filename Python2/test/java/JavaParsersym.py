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
   TK_ClassBodyDeclarationsoptMarker   = 102
   TK_LPGUserActionMarker   = 103
   TK_IntegerLiteral   = 32
   TK_LongLiteral   = 33
   TK_FloatingPointLiteral   = 34
   TK_DoubleLiteral   = 35
   TK_CharacterLiteral   = 36
   TK_StringLiteral   = 37
   TK_MINUS_MINUS   = 26
   TK_OR   = 86
   TK_MINUS   = 46
   TK_MINUS_EQUAL   = 72
   TK_NOT   = 48
   TK_NOT_EQUAL   = 87
   TK_REMAINDER   = 88
   TK_REMAINDER_EQUAL   = 73
   TK_AND   = 68
   TK_AND_AND   = 89
   TK_AND_EQUAL   = 74
   TK_LPAREN   = 3
   TK_RPAREN   = 20
   TK_MULTIPLY   = 69
   TK_MULTIPLY_EQUAL   = 75
   TK_COMMA   = 43
   TK_DOT   = 42
   TK_DIVIDE   = 90
   TK_DIVIDE_EQUAL   = 76
   TK_COLON   = 50
   TK_SEMICOLON   = 4
   TK_QUESTION   = 91
   TK_AT   = 1
   TK_LBRACKET   = 23
   TK_RBRACKET   = 53
   TK_XOR   = 92
   TK_XOR_EQUAL   = 77
   TK_LBRACE   = 27
   TK_OR_OR   = 95
   TK_OR_EQUAL   = 78
   TK_RBRACE   = 45
   TK_TWIDDLE   = 49
   TK_PLUS   = 47
   TK_PLUS_PLUS   = 28
   TK_PLUS_EQUAL   = 79
   TK_LESS   = 24
   TK_LEFT_SHIFT   = 70
   TK_LEFT_SHIFT_EQUAL   = 80
   TK_LESS_EQUAL   = 81
   TK_EQUAL   = 51
   TK_EQUAL_EQUAL   = 93
   TK_GREATER   = 44
   TK_GREATER_EQUAL   = 112
   TK_RIGHT_SHIFT   = 113
   TK_RIGHT_SHIFT_EQUAL   = 114
   TK_UNSIGNED_RIGHT_SHIFT   = 115
   TK_UNSIGNED_RIGHT_SHIFT_EQUAL   = 116
   TK_ELLIPSIS   = 96
   TK_BeginAction   = 104
   TK_EndAction   = 105
   TK_BeginJava   = 106
   TK_EndJava   = 107
   TK_NoAction   = 108
   TK_NullAction   = 109
   TK_BadAction   = 110
   TK_abstract   = 17
   TK_assert   = 57
   TK_boolean   = 5
   TK_break   = 58
   TK_byte   = 6
   TK_case   = 71
   TK_catch   = 97
   TK_char   = 7
   TK_class   = 31
   TK_const   = 117
   TK_continue   = 59
   TK_default   = 67
   TK_do   = 60
   TK_double   = 8
   TK_enum   = 41
   TK_else   = 94
   TK_extends   = 82
   TK_false   = 38
   TK_final   = 19
   TK_finally   = 98
   TK_float   = 9
   TK_for   = 61
   TK_goto   = 118
   TK_if   = 62
   TK_implements   = 111
   TK_import   = 99
   TK_instanceof   = 83
   TK_int   = 10
   TK_interface   = 21
   TK_long   = 11
   TK_native   = 84
   TK_new   = 29
   TK_null   = 39
   TK_package   = 100
   TK_private   = 14
   TK_protected   = 15
   TK_public   = 12
   TK_return   = 63
   TK_short   = 13
   TK_static   = 16
   TK_strictfp   = 18
   TK_super   = 25
   TK_switch   = 64
   TK_synchronized   = 52
   TK_this   = 30
   TK_throw   = 65
   TK_throws   = 101
   TK_transient   = 54
   TK_true   = 40
   TK_try   = 66
   TK_void   = 22
   TK_volatile   = 55
   TK_while   = 56
   TK_EOF_TOKEN   = 85
   TK_IDENTIFIER   = 2
   TK_ERROR_TOKEN   = 119

   orderedTerminalSymbols = [
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

   numTokenKinds   = 119
   isValidForParser  = True

