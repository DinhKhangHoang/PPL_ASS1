#
#Student name: Hoàng Đình Khang
#Student Id: 1711679
#
import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_identifier2(self):
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("aAsVN","aAsVN,<EOF>",103))
    def test_integer4(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",104))
    def test_integer8(self):
        self.assertTrue(TestLexer.checkLexeme("717637ben","717637,ben,<EOF>",108))
    def test_float5(self):
        self.assertTrue(TestLexer.checkLexeme("23.e123","23.e123,<EOF>", 105))
    def test_float6(self):
        self.assertTrue(TestLexer.checkLexeme("23.e","23.,e,<EOF>", 106))
    def test_float7(self):
        self.assertTrue(TestLexer.checkLexeme("067.001E-34khang","067.001E-34,khang,<EOF>",107))
    def test_float9(self):
        self.assertFalse(TestLexer.checkLexeme(".e4",".e4,<EOF>",109))
    def test_float10(self):
        self.assertTrue(TestLexer.checkLexeme(".056e-3aAsVN",".056e-3,aAsVN,<EOF>",110))
    def test_float11(self):
        self.assertTrue(TestLexer.checkLexeme("116.122waitformecomehome","116.122,waitformecomehome,<EOF>",111))
    def test_float12(self):
        self.assertTrue(TestLexer.checkLexeme("12e0_khongdungroi", "12e0,_khongdungroi,<EOF>",112))
    def test_bool13(self):
        self.assertTrue(TestLexer.checkLexeme("true","true,<EOF>",113))
    def test_stringlit14(self):
        self.assertTrue(TestLexer.checkLexeme('"kha\tg"','kha\tg,<EOF>',114))
    def test_stringlit15(self):
        self.assertTrue(TestLexer.checkLexeme("\"Mynameis\"Khang\"", "Mynameis,Khang,Unclosed String: ",115))
    def test_stringlit16(self):
        self.assertTrue(TestLexer.checkLexeme("\"Hello everybody, Im a new student!","Unclosed String: Hello everybody, Im a new student!", 116))
    def test_stringlit17(self):
        self.assertTrue(TestLexer.checkLexeme('"Duong\\nMinh\\bNhu\\tNgoc"','Duong\\nMinh\\bNhu\\tNgoc,<EOF>',117))
    def test_stringlit18(self):
        self.assertTrue(TestLexer.checkLexeme('"No I havent been yet, but i \kwant to!"','Illegal Escape In String: No I havent been yet, but i \k',118))
    def test_comment19(self):
        self.assertTrue(TestLexer.checkLexeme('// Sorry my babe, ahihi','<EOF>', 119))
    def test_comment20(self):
        self.assertTrue(TestLexer.checkLexeme('// a=b+c=d // a==d?','<EOF>',120))
    def test_comment21(self):
        self.assertTrue(TestLexer.checkLexeme('/* This is not a comment','/,*,This,is,not,a,comment,<EOF>',121))
    def test_comment22(self):
        self.assertTrue(TestLexer.checkLexeme("// This comment has a symbol /*", "<EOF>", 122))
    def test_comment23(self):
        self.assertTrue(TestLexer.checkLexeme("/* int a =5; \n b =c */", "<EOF>", 123))
    def test_comment24(self):
        self.assertTrue(TestLexer.checkLexeme("/* foo(a,b,c) \f */goo(g,h,k)", "goo,(,g,,,h,,,k,),<EOF>", 124))
    def test_comment25(self):
        self.assertTrue(TestLexer.checkLexeme("// float a[234]; \n int func1(){}","int,func1,(,),{,},<EOF>",125))
    def test_comment26(self):
        self.assertTrue(TestLexer.checkLexeme("/* this comment is so complex \n // is it a comment", "/,*,this,comment,is,so,complex,<EOF>", 126))
    def test_comment27(self):
        self.assertTrue(TestLexer.checkLexeme("//* comment again and im exhausted","<EOF>", 127))
    def test_comment28(self):
        self.assertTrue(TestLexer.checkLexeme("// this comment has a carriage return \r oh yeah", "oh,yeah,<EOF>",128))
    def test_identifier29(self):
        self.assertTrue(TestLexer.checkLexeme("_","_,<EOF>", 129))
    def test_float30(self):
        self.assertTrue(TestLexer.checkLexeme("23.e-","23.,e,-,<EOF>", 130))
    def test_integer31(self):
        self.assertTrue(TestLexer.checkLexeme("001002003","001002003,<EOF>", 131))
    def test_keyword32(self):
        self.assertTrue(TestLexer.checkLexeme("do while true false","do,while,true,false,<EOF>", 132))
    def test_keyword33(self):
        self.assertTrue(TestLexer.checkLexeme("boolean int float breakcontinue","boolean,int,float,breakcontinue,<EOF>",133))
    def test_keyword34(self):
        self.assertTrue(TestLexer.checkLexeme("string return void if else","string,return,void,if,else,<EOF>",134))
    def test_all35(self):
        self.assertTrue(TestLexer.checkLexeme("void main(){\n\tstring[] getName();}","void,main,(,),{,string,[,],getName,(,),;,},<EOF>",135))
    def test_stringlit36(self):
        self.assertTrue(TestLexer.checkLexeme("\"abc \n abc\"","Unclosed String: abc ",136))
    def test_wrong_token37(self):
        self.assertTrue(TestLexer.checkLexeme("aA?sVN","aA,Error Token ?",137))
    def test_illegal_escape38(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m123" ""","""123,Illegal Escape In String: 123a\\m""",138))
    def test_stringlit39(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\nabc" """, 'Unclosed String: abc', 139))
    def test_unclose_string40(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123 ""","""Unclosed String: 123a\\n123 """,140))
    def test_illegal_escape41(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m123" ""","""123,Illegal Escape In String: 123a\\m""",141))
    def test_double_slash42(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\\\123" ""","""123,123a\\\\123,<EOF>""",142))
    def test_all43(self):
        self.assertTrue(TestLexer.checkLexeme("int main ;", "int,main,;,<EOF>", 143))
    def test_all44(self):
        self.assertTrue(TestLexer.checkLexeme("return i ;","return,i,;,<EOF>", 144))
    def test_all45(self):
        self.assertTrue(TestLexer.checkLexeme("putIntLn ( main ) ;","putIntLn,(,main,),;,<EOF>", 145))
    def test_all46(self):
        self.assertTrue(TestLexer.checkLexeme("d = i + 3 ;","d,=,i,+,3,;,<EOF>", 146))
    def test_all47(self):
        self.assertTrue(TestLexer.checkLexeme("string[] a;","string,[,],a,;,<EOF>", 147))
    def test_all48(self):
        self.assertTrue(TestLexer.checkLexeme("int i[];","int,i,[,],;,<EOF>", 148))
    def test_all49(self):
        self.assertTrue(TestLexer.checkLexeme("print(\"statement\");","print,(,statement,),;,<EOF>", 149))
    def test_all50(self):
        self.assertTrue(TestLexer.checkLexeme("while true;","while,true,;,<EOF>", 150))
    def test_all51(self):
        self.assertTrue(TestLexer.checkLexeme("if ( i >0) {}","if,(,i,>,0,),{,},<EOF>", 151))
    def test_stringlit52(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\" ""","""Unclosed String: abc\\" """, 152))
    def test_stringlit53(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\ " ""","""Illegal Escape In String: abc\ """, 153))
    def test_stringlit54(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\t \\v" ""","""Illegal Escape In String: \\t \\v""", 154))
    def test_stringlit55(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab \n " ""","""Unclosed String: ab """, 155))
    def test_stringlit56(self):
        self.assertTrue(TestLexer.checkLexeme(""" w = "xyz"; abc"; ""","""w,=,xyz,;,abc,Unclosed String: ; """, 156))
    def test_stringlit57(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\" ""","""Unclosed String: abc\\" """, 157))
    def test_all58(self):
        self.assertTrue(TestLexer.checkLexeme(""" for (i = 0; i < size; i=i+1) { } ""","""for,(,i,=,0,;,i,<,size,;,i,=,i,+,1,),{,},<EOF>""", 158))
    def test_all59(self):
        self.assertTrue(TestLexer.checkLexeme("""((((((((((a))))))))));""","""(,(,(,(,(,(,(,(,(,(,a,),),),),),),),),),),;,<EOF>""", 159))
    def test_all60(self):
        self.assertTrue(TestLexer.checkLexeme("""printf("x+y=%d",x+y);""","""printf,(,x+y=%d,,,x,+,y,),;,<EOF>""", 160))
    def test_all61(self):
        self.assertTrue(TestLexer.checkLexeme("""(foo[2])[3];""","""(,foo,[,2,],),[,3,],;,<EOF>""", 161))
    def test_all62(self):
        self.assertTrue(TestLexer.checkLexeme("""return a+b-a-b+a+b;""","""return,a,+,b,-,a,-,b,+,a,+,b,;,<EOF>""", 162))
    def test_all63(self):
        self.assertTrue(TestLexer.checkLexeme("""int add(int a, int b){};""","""int,add,(,int,a,,,int,b,),{,},;,<EOF>""", 163))
    def test_all64(self):
        self.assertTrue(TestLexer.checkLexeme("""x =a[[3]];""","""x,=,a,[,[,3,],],;,<EOF>""", 164))
    def test_all65(self):
        self.assertTrue(TestLexer.checkLexeme("""if ( a==b) f[0] = 1.0 ;""","""if,(,a,==,b,),f,[,0,],=,1.0,;,<EOF>""", 165))
    def test_all66(self):
        self.assertTrue(TestLexer.checkLexeme("""for(j=0;j<n1 && a[j]<=b[i];j=j+1)""","""for,(,j,=,0,;,j,<,n1,&&,a,[,j,],<=,b,[,i,],;,j,=,j,+,1,),<EOF>""", 166))
    def test_all67(self):
        self.assertTrue(TestLexer.checkLexeme("""if ( op == '+') sum = exp1 + exp2;else if ( op == '-') sum = exp1 - exp2;""","""if,(,op,==,Error Token '""", 167))
    def test_all68(self):
        self.assertTrue(TestLexer.checkLexeme("""if ( op == "+") sum = exp1 + exp2;else if ( op == "-") sum = exp1 - exp2;""","""if,(,op,==,+,),sum,=,exp1,+,exp2,;,else,if,(,op,==,-,),sum,=,exp1,-,exp2,;,<EOF>""", 168))
    def test_all69(self):
        self.assertTrue(TestLexer.checkLexeme("""1.2e1 + e - 6.e-3 && .09e-8;""","""1.2e1,+,e,-,6.e-3,&&,.09e-8,;,<EOF>""", 169))
    def test_all70(self):
        self.assertTrue(TestLexer.checkLexeme("""string t[00000010];t = "abc\nabc";""","""string,t,[,00000010,],;,t,=,Unclosed String: abc""", 170))
    def test_all71(self):
        self.assertTrue(TestLexer.checkLexeme("""x = a + (b = f()) + (c = g()) * 7;""","""x,=,a,+,(,b,=,f,(,),),+,(,c,=,g,(,),),*,7,;,<EOF>""", 171))
    def test_all72(self):
        self.assertTrue(TestLexer.checkLexeme("""(A && 3 - B)* -(Z || W) = (A - B/9);""","""(,A,&&,3,-,B,),*,-,(,Z,||,W,),=,(,A,-,B,/,9,),;,<EOF>""", 172))
    def test_all73(self):
        self.assertTrue(TestLexer.checkLexeme("""cout << a<<endl;""","""cout,<,<,a,<,<,endl,;,<EOF>""", 173))
    def test_all74(self):
        self.assertTrue(TestLexer.checkLexeme("""arr[j]   = arr[j+1];""","""arr,[,j,],=,arr,[,j,+,1,],;,<EOF>""", 174))
    def test_all75(self):
        self.assertTrue(TestLexer.checkLexeme("""return (aj*fact[N](aj-1));""","""return,(,aj,*,fact,[,N,],(,aj,-,1,),),;,<EOF>""", 175))
    def test_all76(self):
        self.assertTrue(TestLexer.checkLexeme("""pointer = -(-(-(-(-(b)))));""","""pointer,=,-,(,-,(,-,(,-,(,-,(,b,),),),),),;,<EOF>""", 176))
    def test_all77(self):
        self.assertTrue(TestLexer.checkLexeme("""int[] foo(int a[7])""","""int,[,],foo,(,int,a,[,7,],),<EOF>""", 177))
    def test_all78(self):
        self.assertTrue(TestLexer.checkLexeme("""khong_bit = (a+b)[2];""","""khong_bit,=,(,a,+,b,),[,2,],;,<EOF>""", 178))
    def test_all79(self):
        self.assertTrue(TestLexer.checkLexeme("""1.34[2]+5 - 1e4[42]%1.e5;""","""1.34,[,2,],+,5,-,1e4,[,42,],%,1.e5,;,<EOF>""", 179))
    def test_all80(self):
        self.assertTrue(TestLexer.checkLexeme("""foo(2)+foo()-a[2]*foo((((2+3)-4)/7)-9,0.0,9.7);""","""foo,(,2,),+,foo,(,),-,a,[,2,],*,foo,(,(,(,(,2,+,3,),-,4,),/,7,),-,9,,,0.0,,,9.7,),;,<EOF>""", 180))
    def test_all81(self):
        self.assertTrue(TestLexer.checkLexeme("""if(a) if(b) c;else d;e;""","""if,(,a,),if,(,b,),c,;,else,d,;,e,;,<EOF>""", 181))
    def test_all82(self):
        self.assertTrue(TestLexer.checkLexeme("""a= =c;""","""a,=,=,c,;,<EOF>""", 182))
    def test_all83(self):
        self.assertTrue(TestLexer.checkLexeme("""a= b&&c||d&&e||i=f+g!=h;""","""a,=,b,&&,c,||,d,&&,e,||,i,=,f,+,g,!=,h,;,<EOF>""", 183))
    def test_all84(self):
        self.assertTrue(TestLexer.checkLexeme("""a=1*2*3*4*5*6*7*8 % a % a % a % a;""","""a,=,1,*,2,*,3,*,4,*,5,*,6,*,7,*,8,%,a,%,a,%,a,%,a,;,<EOF>""", 184))
    def test_all85(self):
        self.assertTrue(TestLexer.checkLexeme("""a= b != (c [0] + d)*a;""","""a,=,b,!=,(,c,[,0,],+,d,),*,a,;,<EOF>""", 185))
    def test_all86(self):
        self.assertTrue(TestLexer.checkLexeme("""a[b[c[d[e[4]]]]]=0;""","""a,[,b,[,c,[,d,[,e,[,4,],],],],],=,0,;,<EOF>""", 186))
    def test_all87(self):
        self.assertTrue(TestLexer.checkLexeme("""foo(2,true)[3+x] = a[b[2]];""","""foo,(,2,,,true,),[,3,+,x,],=,a,[,b,[,2,],],;,<EOF>""", 187))
    def test_all88(self):
        self.assertTrue(TestLexer.checkLexeme("""int foo(int a){a = {int i;};}""","""int,foo,(,int,a,),{,a,=,{,int,i,;,},;,},<EOF>""", 188))
    def test_all89(self):
        self.assertTrue(TestLexer.checkLexeme("""string a;a ="234 876";""","""string,a,;,a,=,234 876,;,<EOF>""", 189))
    def test_all90(self):
        self.assertTrue(TestLexer.checkLexeme("""if(num <= 1 || (num % 2 ==0 && num != 2))return false;""","""if,(,num,<=,1,||,(,num,%,2,==,0,&&,num,!=,2,),),return,false,;,<EOF>""", 190))
    def test_all91(self):
        self.assertTrue(TestLexer.checkLexeme("""b = true && "string" || false == (1e6 - 3);""","""b,=,true,&&,string,||,false,==,(,1e6,-,3,),;,<EOF>""", 191))
    def test_all92(self):
        self.assertTrue(TestLexer.checkLexeme("""for ( k = 1 ; k < space ; k=k+1 )printf(" ");space=space-1;""","""for,(,k,=,1,;,k,<,space,;,k,=,k,+,1,),printf,(, ,),;,space,=,space,-,1,;,<EOF>""", 192))
    def test_all93(self):
        self.assertTrue(TestLexer.checkLexeme("""printf("%d is a positive number \\n", num);""","""printf,(,%d is a positive number \\n,,,num,),;,<EOF>""", 193))
    def test_errorchar94(self):
        self.assertTrue(TestLexer.checkLexeme("""int a ? =6;""","""int,a,Error Token ?""", 194))
    def test_errorchar95(self):
        self.assertTrue(TestLexer.checkLexeme("""float b => c;""","""float,b,=,>,c,;,<EOF>""", 195))
    def test_errorchar96(self):
        self.assertTrue(TestLexer.checkLexeme("""\\b\\t""","""Error Token \\""", 196))
    def test_comment97(self):
        self.assertTrue(TestLexer.checkLexeme("""//\\b\\t""","""<EOF>""", 197))
    def test_errorchar98(self):
        self.assertTrue(TestLexer.checkLexeme("""/ / \\b\\t""","""/,/,Error Token \\""", 198))
    def test_errorchar99(self):
        self.assertTrue(TestLexer.checkLexeme("""'khang'""","""Error Token '""", 199))
    def test_errorchar100(self):
        self.assertTrue(TestLexer.checkLexeme(""".khang.dat.trung.""","""Error Token .""", 200))
    