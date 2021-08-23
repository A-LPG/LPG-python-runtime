%options automatic_ast=nested,variables=nt,visitor=preorder
%options programming_language=python3
%options template= btParserTemplateF.gi

$Terminals
 IntegerLiteral
 PLUS ::= +
 MULTIPLY ::= *
 LPAREN ::= (
 RPAREN ::= )
$end
$Rules
 E ::= E + T
 | T
 T ::= T * F
 | F
 F ::= IntegerLiteral
 F$ParenExpr ::= ( E )
$End