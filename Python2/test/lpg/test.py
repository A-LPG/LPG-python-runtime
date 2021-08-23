#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from LPGLexer import  LPGLexer
from LPGParser import  LPGParser

if __name__ == '__main__':
    _lexer = LPGLexer("jikespg.g")
    parser = LPGParser(_lexer.getILexStream())
    _lexer.printTokens = True
    _lexer.lexer(parser.getIPrsStream())
    ast = parser.parser()
    if ast:
        print("成功")
    else:
        print("失败")
