# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\60")
        buf.write("\u0166\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\6\37\u00da\n\37\r\37\16\37\u00db")
        buf.write("\3 \6 \u00df\n \r \16 \u00e0\3!\3!\5!\u00e5\n!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\5\"\u00ed\n\"\3\"\3\"\3\"\5\"\u00f2\n\"")
        buf.write("\3\"\3\"\3\"\5\"\u00f7\n\"\3\"\3\"\3\"\5\"\u00fc\n\"\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0107\n#\3$\6$\u010a\n$\r")
        buf.write("$\16$\u010b\3%\3%\3%\7%\u0111\n%\f%\16%\u0114\13%\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\7\'\u011e\n\'\f\'\16\'\u0121\13")
        buf.write("\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\6\60\u0134\n\60\r\60\16\60\u0135\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\7\61\u013e\n\61\f\61\16\61\u0141\13\61\3\61")
        buf.write("\3\61\3\61\3\61\7\61\u0147\n\61\f\61\16\61\u014a\13\61")
        buf.write("\3\61\3\61\5\61\u014e\n\61\3\61\3\61\3\62\3\62\3\62\7")
        buf.write("\62\u0155\n\62\f\62\16\62\u0158\13\62\3\63\3\63\3\63\7")
        buf.write("\63\u015d\n\63\f\63\16\63\u0160\13\63\3\63\3\63\3\63\3")
        buf.write("\64\3\64\3\u0148\2\65\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\2=")
        buf.write("\2?\2A\2C\37E G!I\"K\2M#O$Q%S&U\'W(Y)[*]+_,a-c.e/g\60")
        buf.write("\3\2\n\3\2\62;\4\2GGgg\6\2\f\f\17\17$$^^\t\2$$^^ddhhp")
        buf.write("pttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\4\2")
        buf.write("\f\f\17\17\2\u0176\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3")
        buf.write("\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[")
        buf.write("\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2")
        buf.write("e\3\2\2\2\2g\3\2\2\2\3i\3\2\2\2\5m\3\2\2\2\7r\3\2\2\2")
        buf.write("\tz\3\2\2\2\13\u0080\3\2\2\2\r\u0089\3\2\2\2\17\u008e")
        buf.write("\3\2\2\2\21\u0092\3\2\2\2\23\u0098\3\2\2\2\25\u009b\3")
        buf.write("\2\2\2\27\u00a2\3\2\2\2\31\u00a5\3\2\2\2\33\u00ab\3\2")
        buf.write("\2\2\35\u00b2\3\2\2\2\37\u00b4\3\2\2\2!\u00b6\3\2\2\2")
        buf.write("#\u00b8\3\2\2\2%\u00ba\3\2\2\2\'\u00bc\3\2\2\2)\u00be")
        buf.write("\3\2\2\2+\u00c1\3\2\2\2-\u00c4\3\2\2\2/\u00c7\3\2\2\2")
        buf.write("\61\u00ca\3\2\2\2\63\u00cc\3\2\2\2\65\u00ce\3\2\2\2\67")
        buf.write("\u00d1\3\2\2\29\u00d4\3\2\2\2;\u00d6\3\2\2\2=\u00d9\3")
        buf.write("\2\2\2?\u00de\3\2\2\2A\u00e2\3\2\2\2C\u00fb\3\2\2\2E\u0106")
        buf.write("\3\2\2\2G\u0109\3\2\2\2I\u010d\3\2\2\2K\u0118\3\2\2\2")
        buf.write("M\u011b\3\2\2\2O\u0122\3\2\2\2Q\u0124\3\2\2\2S\u0126\3")
        buf.write("\2\2\2U\u0128\3\2\2\2W\u012a\3\2\2\2Y\u012c\3\2\2\2[\u012e")
        buf.write("\3\2\2\2]\u0130\3\2\2\2_\u0133\3\2\2\2a\u014d\3\2\2\2")
        buf.write("c\u0151\3\2\2\2e\u0159\3\2\2\2g\u0164\3\2\2\2ij\7k\2\2")
        buf.write("jk\7p\2\2kl\7v\2\2l\4\3\2\2\2mn\7x\2\2no\7q\2\2op\7k\2")
        buf.write("\2pq\7f\2\2q\6\3\2\2\2rs\7d\2\2st\7q\2\2tu\7q\2\2uv\7")
        buf.write("n\2\2vw\7g\2\2wx\7c\2\2xy\7p\2\2y\b\3\2\2\2z{\7d\2\2{")
        buf.write("|\7t\2\2|}\7g\2\2}~\7c\2\2~\177\7m\2\2\177\n\3\2\2\2\u0080")
        buf.write("\u0081\7e\2\2\u0081\u0082\7q\2\2\u0082\u0083\7p\2\2\u0083")
        buf.write("\u0084\7v\2\2\u0084\u0085\7k\2\2\u0085\u0086\7p\2\2\u0086")
        buf.write("\u0087\7w\2\2\u0087\u0088\7g\2\2\u0088\f\3\2\2\2\u0089")
        buf.write("\u008a\7g\2\2\u008a\u008b\7n\2\2\u008b\u008c\7u\2\2\u008c")
        buf.write("\u008d\7g\2\2\u008d\16\3\2\2\2\u008e\u008f\7h\2\2\u008f")
        buf.write("\u0090\7q\2\2\u0090\u0091\7t\2\2\u0091\20\3\2\2\2\u0092")
        buf.write("\u0093\7h\2\2\u0093\u0094\7n\2\2\u0094\u0095\7q\2\2\u0095")
        buf.write("\u0096\7c\2\2\u0096\u0097\7v\2\2\u0097\22\3\2\2\2\u0098")
        buf.write("\u0099\7k\2\2\u0099\u009a\7h\2\2\u009a\24\3\2\2\2\u009b")
        buf.write("\u009c\7t\2\2\u009c\u009d\7g\2\2\u009d\u009e\7v\2\2\u009e")
        buf.write("\u009f\7w\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7p\2\2\u00a1")
        buf.write("\26\3\2\2\2\u00a2\u00a3\7f\2\2\u00a3\u00a4\7q\2\2\u00a4")
        buf.write("\30\3\2\2\2\u00a5\u00a6\7y\2\2\u00a6\u00a7\7j\2\2\u00a7")
        buf.write("\u00a8\7k\2\2\u00a8\u00a9\7n\2\2\u00a9\u00aa\7g\2\2\u00aa")
        buf.write("\32\3\2\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7v\2\2\u00ad")
        buf.write("\u00ae\7t\2\2\u00ae\u00af\7k\2\2\u00af\u00b0\7p\2\2\u00b0")
        buf.write("\u00b1\7i\2\2\u00b1\34\3\2\2\2\u00b2\u00b3\7-\2\2\u00b3")
        buf.write("\36\3\2\2\2\u00b4\u00b5\7,\2\2\u00b5 \3\2\2\2\u00b6\u00b7")
        buf.write("\7/\2\2\u00b7\"\3\2\2\2\u00b8\u00b9\7\61\2\2\u00b9$\3")
        buf.write("\2\2\2\u00ba\u00bb\7#\2\2\u00bb&\3\2\2\2\u00bc\u00bd\7")
        buf.write("\'\2\2\u00bd(\3\2\2\2\u00be\u00bf\7~\2\2\u00bf\u00c0\7")
        buf.write("~\2\2\u00c0*\3\2\2\2\u00c1\u00c2\7(\2\2\u00c2\u00c3\7")
        buf.write("(\2\2\u00c3,\3\2\2\2\u00c4\u00c5\7#\2\2\u00c5\u00c6\7")
        buf.write("?\2\2\u00c6.\3\2\2\2\u00c7\u00c8\7?\2\2\u00c8\u00c9\7")
        buf.write("?\2\2\u00c9\60\3\2\2\2\u00ca\u00cb\7>\2\2\u00cb\62\3\2")
        buf.write("\2\2\u00cc\u00cd\7@\2\2\u00cd\64\3\2\2\2\u00ce\u00cf\7")
        buf.write(">\2\2\u00cf\u00d0\7?\2\2\u00d0\66\3\2\2\2\u00d1\u00d2")
        buf.write("\7@\2\2\u00d2\u00d3\7?\2\2\u00d38\3\2\2\2\u00d4\u00d5")
        buf.write("\7?\2\2\u00d5:\3\2\2\2\u00d6\u00d7\7\60\2\2\u00d7<\3\2")
        buf.write("\2\2\u00d8\u00da\t\2\2\2\u00d9\u00d8\3\2\2\2\u00da\u00db")
        buf.write("\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write(">\3\2\2\2\u00dd\u00df\t\2\2\2\u00de\u00dd\3\2\2\2\u00df")
        buf.write("\u00e0\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1@\3\2\2\2\u00e2\u00e4\t\3\2\2\u00e3\u00e5\7/\2\2")
        buf.write("\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\3")
        buf.write("\2\2\2\u00e6\u00e7\5=\37\2\u00e7B\3\2\2\2\u00e8\u00e9")
        buf.write("\5=\37\2\u00e9\u00ea\5;\36\2\u00ea\u00ec\5? \2\u00eb\u00ed")
        buf.write("\5A!\2\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00fc")
        buf.write("\3\2\2\2\u00ee\u00ef\5;\36\2\u00ef\u00f1\5? \2\u00f0\u00f2")
        buf.write("\5A!\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00fc")
        buf.write("\3\2\2\2\u00f3\u00f4\5=\37\2\u00f4\u00f6\5;\36\2\u00f5")
        buf.write("\u00f7\5A!\2\u00f6\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write("\u00fc\3\2\2\2\u00f8\u00f9\5=\37\2\u00f9\u00fa\5A!\2\u00fa")
        buf.write("\u00fc\3\2\2\2\u00fb\u00e8\3\2\2\2\u00fb\u00ee\3\2\2\2")
        buf.write("\u00fb\u00f3\3\2\2\2\u00fb\u00f8\3\2\2\2\u00fcD\3\2\2")
        buf.write("\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7")
        buf.write("w\2\2\u0100\u0107\7g\2\2\u0101\u0102\7h\2\2\u0102\u0103")
        buf.write("\7c\2\2\u0103\u0104\7n\2\2\u0104\u0105\7u\2\2\u0105\u0107")
        buf.write("\7g\2\2\u0106\u00fd\3\2\2\2\u0106\u0101\3\2\2\2\u0107")
        buf.write("F\3\2\2\2\u0108\u010a\t\2\2\2\u0109\u0108\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2")
        buf.write("\u010cH\3\2\2\2\u010d\u0112\7$\2\2\u010e\u0111\n\4\2\2")
        buf.write("\u010f\u0111\5K&\2\u0110\u010e\3\2\2\2\u0110\u010f\3\2")
        buf.write("\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u0112\3\2\2\2\u0115")
        buf.write("\u0116\7$\2\2\u0116\u0117\b%\2\2\u0117J\3\2\2\2\u0118")
        buf.write("\u0119\7^\2\2\u0119\u011a\t\5\2\2\u011aL\3\2\2\2\u011b")
        buf.write("\u011f\t\6\2\2\u011c\u011e\t\7\2\2\u011d\u011c\3\2\2\2")
        buf.write("\u011e\u0121\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3")
        buf.write("\2\2\2\u0120N\3\2\2\2\u0121\u011f\3\2\2\2\u0122\u0123")
        buf.write("\7*\2\2\u0123P\3\2\2\2\u0124\u0125\7+\2\2\u0125R\3\2\2")
        buf.write("\2\u0126\u0127\7}\2\2\u0127T\3\2\2\2\u0128\u0129\7\177")
        buf.write("\2\2\u0129V\3\2\2\2\u012a\u012b\7=\2\2\u012bX\3\2\2\2")
        buf.write("\u012c\u012d\7]\2\2\u012dZ\3\2\2\2\u012e\u012f\7_\2\2")
        buf.write("\u012f\\\3\2\2\2\u0130\u0131\7.\2\2\u0131^\3\2\2\2\u0132")
        buf.write("\u0134\t\b\2\2\u0133\u0132\3\2\2\2\u0134\u0135\3\2\2\2")
        buf.write("\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137\3")
        buf.write("\2\2\2\u0137\u0138\b\60\3\2\u0138`\3\2\2\2\u0139\u013a")
        buf.write("\7\61\2\2\u013a\u013b\7\61\2\2\u013b\u013f\3\2\2\2\u013c")
        buf.write("\u013e\n\t\2\2\u013d\u013c\3\2\2\2\u013e\u0141\3\2\2\2")
        buf.write("\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u014e\3")
        buf.write("\2\2\2\u0141\u013f\3\2\2\2\u0142\u0143\7\61\2\2\u0143")
        buf.write("\u0144\7,\2\2\u0144\u0148\3\2\2\2\u0145\u0147\13\2\2\2")
        buf.write("\u0146\u0145\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0149\3")
        buf.write("\2\2\2\u0148\u0146\3\2\2\2\u0149\u014b\3\2\2\2\u014a\u0148")
        buf.write("\3\2\2\2\u014b\u014c\7,\2\2\u014c\u014e\7\61\2\2\u014d")
        buf.write("\u0139\3\2\2\2\u014d\u0142\3\2\2\2\u014e\u014f\3\2\2\2")
        buf.write("\u014f\u0150\b\61\3\2\u0150b\3\2\2\2\u0151\u0156\7$\2")
        buf.write("\2\u0152\u0155\n\4\2\2\u0153\u0155\5K&\2\u0154\u0152\3")
        buf.write("\2\2\2\u0154\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157d\3\2\2\2\u0158\u0156")
        buf.write("\3\2\2\2\u0159\u015e\7$\2\2\u015a\u015d\n\4\2\2\u015b")
        buf.write("\u015d\5K&\2\u015c\u015a\3\2\2\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f\u0161\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162\7")
        buf.write("^\2\2\u0162\u0163\n\5\2\2\u0163f\3\2\2\2\u0164\u0165\13")
        buf.write("\2\2\2\u0165h\3\2\2\2\27\2\u00db\u00e0\u00e4\u00ec\u00f1")
        buf.write("\u00f6\u00fb\u0106\u010b\u0110\u0112\u011f\u0135\u013f")
        buf.write("\u0148\u014d\u0154\u0156\u015c\u015e\4\3%\2\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    VOIDTYPE = 2
    BOOLEAN = 3
    BREAK = 4
    CONTINUE = 5
    ELSE = 6
    FOR = 7
    FLOATTYPE = 8
    IF = 9
    RETURN = 10
    DO = 11
    WHILE = 12
    STRING = 13
    ADD = 14
    MUL = 15
    SUB = 16
    DIV = 17
    NOT = 18
    MOD = 19
    OR = 20
    AND = 21
    NEQ = 22
    EQ = 23
    LT = 24
    GT = 25
    LE = 26
    GE = 27
    ASSIGN = 28
    FLOATLIT = 29
    BOOLLIT = 30
    INTLIT = 31
    STRINGLIT = 32
    ID = 33
    LB = 34
    RB = 35
    LP = 36
    RP = 37
    SEMI = 38
    LSB = 39
    RSB = 40
    CM = 41
    WS = 42
    COMMENT = 43
    UNCLOSE_STRING = 44
    ILLEGAL_ESCAPE = 45
    ERROR_CHAR = 46

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'void'", "'boolean'", "'break'", "'continue'", "'else'", 
            "'for'", "'float'", "'if'", "'return'", "'do'", "'while'", "'string'", 
            "'+'", "'*'", "'-'", "'/'", "'!'", "'%'", "'||'", "'&&'", "'!='", 
            "'=='", "'<'", "'>'", "'<='", "'>='", "'='", "'('", "')'", "'{'", 
            "'}'", "';'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "BOOLEAN", "BREAK", "CONTINUE", "ELSE", 
            "FOR", "FLOATTYPE", "IF", "RETURN", "DO", "WHILE", "STRING", 
            "ADD", "MUL", "SUB", "DIV", "NOT", "MOD", "OR", "AND", "NEQ", 
            "EQ", "LT", "GT", "LE", "GE", "ASSIGN", "FLOATLIT", "BOOLLIT", 
            "INTLIT", "STRINGLIT", "ID", "LB", "RB", "LP", "RP", "SEMI", 
            "LSB", "RSB", "CM", "WS", "COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "INTTYPE", "VOIDTYPE", "BOOLEAN", "BREAK", "CONTINUE", 
                  "ELSE", "FOR", "FLOATTYPE", "IF", "RETURN", "DO", "WHILE", 
                  "STRING", "ADD", "MUL", "SUB", "DIV", "NOT", "MOD", "OR", 
                  "AND", "NEQ", "EQ", "LT", "GT", "LE", "GE", "ASSIGN", 
                  "Point", "Number", "Fraction", "Exponent", "FLOATLIT", 
                  "BOOLLIT", "INTLIT", "STRINGLIT", "ESCAPESEQUENCE", "ID", 
                  "LB", "RB", "LP", "RP", "SEMI", "LSB", "RSB", "CM", "WS", 
                  "COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text[1:]);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text[1:]);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text);
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[35] = self.STRINGLIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    self.text= self.text[1:-1]

     


