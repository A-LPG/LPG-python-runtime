#!/usr/bin/env python
# -*- coding: utf-8 -*-
from JavaLexer import  JavaLexer
from JavaParser import  JavaParser

if __name__ == '__main__':
    _lexer = JavaLexer("test2.java")
    parser = JavaParser(_lexer.getILexStream())
    _lexer.printTokens = True
    _lexer.lexer(parser.getIPrsStream())
    ast = parser.parser()
    if ast:
        print("成功")
    else:
        print("失败")
