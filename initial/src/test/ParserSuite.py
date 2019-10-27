#
#Student name: Hoàng Đình Khang
#Student Id: 1711679
#
import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_funcall2(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_program_expression4(self):
        input = """int main(){
            foo(2)[3+x] = a[b[2]] + 3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_vardecl5(self):
        input = """void main(){
            string[] a;
        }"""
        expect = "Error on line 2 col 18: ["
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_all6(self):
        input ="""int foo (int a , float b []){
            boolean c ;
            int i ;
            i = a + 3 ;
            if ( i >0) {
                    int d ;
                    d = i + 3 ;
                    putInt (d ) ;
            }
            return i ;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_all7(self):
        input ="""int i ;
        int f ( ) {
            return 200;
        }
        void main ( ) {
            int main ;
            main = f ( ) ;
            putIntLn ( main ) ;
            {
                int i ;
                int main ;
                int f ;
                main = f = i = 100;
                putIntLn ( i ) ;
                putIntLn ( main ) ;
                putIntLn ( f ) ;
            }
            putIntLn ( main ) ;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_vardecl8(self):
        input ="""void main(){
        int i[];
        }"""
        expect="Error on line 2 col 14: ]"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_ifstmt9(self):
        input ="""void main( ){ if (a) if (b) if (c) a; else a; else }"""
        expect="Error on line 1 col 51: }"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_whilestmt10(self):
        input ="""void main() {
            do {
            print("statement 1");
            }
            {
            print("statement 2");
            }
            while true;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_comment11(self):
        input ="""int main()
        {
        /* printf function displays the content that is
            * passed between the double quotes.
            */
        printf("Hello World");
        return 0;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_ifstmt12(self):
        input ="""void main()
        {
            int num;
            printf("Enter a number: \\n");
            scanf("%d", num);
            if (num > 0)
                printf("%d is a positive number \\n", num);
            else if (num < 0)
                printf("%d is a negative number \\n", num);
            else
                printf("0 is neither positive nor negative");
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_indexarray13(self):
        input ="""int main(){
            (foo[2])[3];
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_indexarray14(self):
        input ="""int main(){
            foo[2][3];
        }"""
        expect="Error on line 2 col 18: ["
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_all15(self):
        input ="""int main()
        {
            int number;
            // printf() dislpays the formatted output 
            printf("Enter an integer: ");  
            
            // scanf() reads the formatted input and stores them
            scanf("%d", number);  
            
            // printf() displays the formatted output
            printf("You entered: %d", number);
            return 0;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_declaration16(self):
        input ="""int x;
        float y;
        int main(){
            printf("x+y=%d",x+y);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_forstmt17(self):
        input ="""int main()
        {
            int number, i;
            printf("Enter a positive integer: ");
            scanf("%d",number);
            printf("Factors of %d are: ", number);
            for(i=1; i <= number; i=i+1)
            {
                if (number%i == 0)
                {
                    printf("%d ",i);
                }
            }
            return 0;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_ifstmt18(self):
        input ="""int main()
        {
            float n1, n2, n3;
            printf("Enter three different numbers: ");
            scanf("%lf %lf %lf", n1, n2, n3);
            if( n1>=n2 && n1>=n3 )
                printf("%.2f is the largest number.", n1);
            if( n2>=n1 && n2>=n3 )
                printf("%.2f is the largest number.", n2);
            if( n3>=n1 && n3>=n2 )
                printf("%.2f is the largest number.", n3);
            return 0;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_all19(self):
        input ="""int main() { 
            // loop from 1 to 10  
            for (i = 1; i <= 10; i=i+1) {  
                // If i is equals to 6,  
                // continue to next iteration  
                // without printing  
                if (i == 6)  
                    continue;  
                else
                    // otherwise print the value of i  
                    printf("%d ", i);  
            }
            return 0;  
        } """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_all20(self):
        input ="""void findElement(int arr[], int size, int key) 
        { 
            // loop to traverse array and search for key 
            for (i = 0; i < size; i=i+1) { 
                if (arr[i] == key) { 
                    printf("Element found at position: %d", (i + 1));
                    // using break to terminate loop execution 
                    break; 
                } 
            }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_subexpression21(self):
        input ="""void main(){
            ((((((((((a))))))))));
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_expression22(self):
        input ="""void main(){
            x=a+b*(-c);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_expression23(self):
        input ="""void main(){
            x=(a+b)*(-c);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_all24(self):
        input ="""int main(){
            int i,j;
            float f;

            i = 5; j = 2;
            f = 3.0;

            f = f + j / i;
            printf("value of f is %f\\n", f);
            exit(EXIT_SUCCESS);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_expression25(self):
        input ="""int main(){
            a=100=a+b;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_whilestmt26(self):
        input ="""int main(){
            do
            {
                a+b;
            }
            {
                b+c;
            }
            while true=false;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_funcall27(self):
        input ="""int main(){
            foo(foo(foo(foo(foo(foo(foo(foo(0))))))));
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_expression28(self):
        input ="""int main(){
            x=a && b == c;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_indexarray29(self):
        input ="""int main(){
            x=goo[goo[goo[goo[goo[goo]]]]];
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_expression30(self):
        input ="""int main(){
            x=1*5/9-8*6+7+2;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_ifstmt31(self):
        input ="""int main(){
            if (var1 != var2)
        {
            printf("var1 is not equal to var2");
            //Nested if else
            if (var1 > var2)
            {
                printf("var1 is greater than var2");
            }
            else
            {
                printf("var2 is greater than var1");
            }
        }
        else
        {
            printf("var1 is equal to var2");
        }
        return 0;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_vardecl32(self):
        input ="""int main(){
            int x = 5, a,b,c;
        }"""
        expect="Error on line 2 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_vardecl33(self):
        input ="""int main(){
            int 5;
        }"""
        expect="Error on line 2 col 16: 5"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_funcdecl34(self):
        input ="""int main(){
            int result;
        }
        float add(float a,float b){
            return a+b-a-b+a+b;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_parameterdecl35(self):
        input ="""int main(){
            int result;
        }
        float add(float a,x,float b){
            return a+b-a-b+a+b;
        }"""
        expect="Error on line 4 col 26: x"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_functiondecl36(self):
        input ="""int main(){
            int result;
            int add(int a, int b){

            };
        }"""
        expect="Error on line 3 col 19: ("
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_indexarray37(self):
        input ="""int main(){
            x =a[[3]];
        }"""
        expect="Error on line 2 col 17: ["
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_parameterdecl38(self):
        input ="""int main(float[1]b, int c){
            x =a[b[3]];
        }"""
        expect="Error on line 1 col 14: ["
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_indexarray39(self):
        input ="""int main(float b[]){
            x =a[b[3]];
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_comment40(self):
        input ="""int main(float b){
            /* this comment
            * will be skip*/
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_comment41(self):
        input ="""int main(float b){
            /* this comment
            * will be skip*/
            * except this */
        }"""
        expect="Error on line 4 col 12: *"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_vardecl42(self):
        input ="""int main(){
            int x[];
        }"""
        expect="Error on line 2 col 18: ]"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_expression43(self):
        input ="""int main(){
            y=false;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_ifstmt44(self):
        input ="""int main(){
            if()
            a;
        }"""
        expect="Error on line 2 col 15: )"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_all45(self):
        input ="""int main(){
            int a , b , c ;
            a=b=c=5;
            float f [5] ;
            if ( a==b) 
                f[0] = 1.0 ;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_forstmt46(self):
        input ="""int main()
        {
        for (i=0; i<2; i=i+1)
        {
            for (j=0; j<4; j=j+1)
            {
            printf("%d, %d\\n",i ,j);
            }
        }
        return 0;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_forstmt47(self):
        input ="""int main() {
        int i, j;
        int table;
        int max;
        for (i = 1; i <= table; i=i+1) { // outer loop
        for (j = 0; j <= max; j=j+1) { // inner loop
            printf("%d x %d = %d\\n", i, j, i*j);
        }
        printf("\\n"); /* blank line between tables */
        }}"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_forstmt48(self):
        input ="""int main()
        {
        
            /* count down from 10*/
            int waits;
            int s;
            for(s = waits; s > 0; s=s-1)
            {
                printf("%d\\n",s);
            }
            printf("Happy New Year!\\n");
        
            /* count by 3*/
            for(s = 0; s < 10; s=s+3)
            {
                printf("%d\\n",s);
            }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_forstmt49(self):
        input ="""int main(){
            for ( i = 1 ; i <= levels ; i=i+1 )
            {
                for ( k = 1 ; k < space ; k=k+1 )
                    printf(" ");
                space=space-1;
        
                for ( k = 1 ; k <= 2*i - 1 ; k=k+1 )
                    printf("*");
                printf("\\n");
            }
        return 0;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_expression50(self):
        input ="""int main(){
            a= =c;
        }"""
        expect="Error on line 2 col 15: ="
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_ifstmt51(self):
        input ="""int main(){
            if(a)
                if(b)
                    c;
                else
                    d;
            e;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_ifstmt52(self):
        input ="""int main(){
            if(a)
                if(b)
                    if(f)
                        g;
                    else
                        h;
                else
                    d;
            e;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_ifstmt53(self):
        input ="""int main(){
            if(a)
                b;
            else
                if (c)
                    d;
                else
                    if(e)
                        f;
            return 0;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_expression54(self):
        input ="""int main(){
            a= b&&c||d&&e||i=f+g!=h;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_expression55(self):
        input ="""int main(){
            a= !b<=c;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_expression55(self):
        input ="""int main(){
            a= !b<=c;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_expression56(self):
        input="""int main(){
            a= b > c = d = g != f[7] * y;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_expression57(self):
        input="""int main(){
            a=1*2*3*4*5*6*7*8 % a % a % a % a;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_expression58(self):
        input="""int main(){
            a+c= (3 < 4) + (6 == 64 / 4);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_expression59(self):
        input="""int main(){
            a= b == c != d;
        }"""
        expect="Error on line 2 col 22: !="
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_expression60(self):
        input="""int main(){
            a= b <= c >= d;
        }"""
        expect="Error on line 2 col 22: >="
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_expression61(self):
        input="""int main(){
            a= b != (c [0] + d)*a;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_expression62(self):
        input="""int main(){
            pointer = &b;
        }"""
        expect="&"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_expression63(self):
        input="""int main(){
            pointer = &&b;
        }"""
        expect="Error on line 2 col 22: &&"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_expression64(self):
        input="""int main(){
            pointer = -------b;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_expression65(self):
        input="""int main(){
            pointer = -(-(-(-(-(b)))));
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_expression66(self):
        input="""int main(){
            pointer = -(!(-(!(-(-!b)))));
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_expression67(self):
        input="""int main(){
            (A && 3 - B)* -(Z || W) = (A - B/9);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_expression68(self):
        input="""int main(){
            x = a + (b = f()) + (c = g()) * 7;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_expression69(self):
        input="""int main(){
            cout << a<<endl;
        }"""
        expect="Error on line 2 col 18: <"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_all70(self):
        input="""int main(){
            if ( op == '+') sum = exp1 + exp2;
            else if ( op == '-') sum = exp1 - exp2;
            else if ( op == '/') sum = exp1 / exp2;
            else if ( op == '*') sum = exp1 * exp2;
        }"""
        expect="'"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_all71(self):
        input="""int main(){
            if ( op == "+") sum = exp1 + exp2;
            else if ( op == "-") sum = exp1 - exp2;
            else if ( op == "/") sum = exp1 / exp2;
            else if ( op == "*") sum = exp1 * exp2;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_all72(self):
        input="""int main(){
            do {
                /* after parsing string, it must contain only digits */
                if (!valid_digit(ptr))
                    return 0;
                num = atoi(ptr);
                /* check for valid IP */
                if (num >= 0 && num <= 255) {
                    /* parse remaining string */
                    ptr = strtok(NULL, DELIM);
                    if (ptr != NULL)
                        dots;
                } else
                    return 0;
            }while (ptr);
            /* valid IP string must contain 3 dots */
            if (dots != 3)
                return 0;
            return 1;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_program73(self):
        input="""a=foo(5)[8];"""
        expect="Error on line 1 col 0: a"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_all74(self):
        input="""int main(){
            sort(begin(),end()); 
            for(i=0;i<n2;i=i+1){
                for(j=0;j<n1 && a[j]<=b[i];j=j+1){
                    // elements of sorted a is entered to array c 
                    // maintaing the element order as in b
                    if(a[j]==b[i]){
                        push_back(a[j]);
                        //clear the element pushed into c
                        a[j]=0;
                    }
                }
            }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_whilestmt75(self):
        input="""int main(){
            do{
                arr[i=i+1]=c;
                scanf("%c",c);
            }while(c!="\\n");
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_all76(self):
        input="""int fact(int aj)
        {
            if(aj==1 || aj==0)
                return 1;
            else
                return (aj*fact(aj-1));
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_all77(self):
        input="""int fact(int aj)
        {
            if(aj==1 || aj==0)
                return 1;
            else
                return (aj*fact[N](aj-1));
        }"""
        expect="Error on line 6 col 34: ("
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_forstmt78(self):
        input="""int fact(int aj)
        {
            for(i =0;i < 10;i=i+1){
                n = n+ i;
            };
        }"""
        expect="Error on line 5 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_forstmt79(self):
        input="""int main(){
            for(i =0,j=0;i+j < 10;i=i+1,j=j+1){
                n = n+ i;
            };
        }"""
        expect="Error on line 2 col 20: ,"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_floatlit80(self):
        input="""int main(){
            1.2e1 + e - 6.e-3 && .09e-8;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_floatlit81(self):
        input="""int main(){
            1.2e1 + .e - 6.e-3 && .09e-8;
        }"""
        expect="."
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_floatlit82(self):
        input="""int main(){
            1.2e1 + 1.e - 6.e-3 && .09e-8;
        }"""
        expect="Error on line 2 col 22: e"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_floatlit83(self):
        input="""int main(){
            1.2e1 + 1.e-6.e-3 && .09e-8;
        }"""
        expect="."
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_floatlit84(self):
        input="""int main(){
            1.2e1 + 1.e-6-8.e-3 && .09e-8;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_floatlit85(self):
        input="""int main(){
            1.2e1 + 1.e-6-8.e+3 && .09e-8;
        }"""
        expect="Error on line 2 col 28: e"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_vardecl86(self):
        input="""int main(){
            string t[N];
            t = "abc\nabc";
        }"""
        expect="Error on line 2 col 21: N"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_stringlit87(self):
        input="""int main(){
            string t[00000010];
            t = "abc\nabc";
        }"""
        expect="abc"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_stringlit88(self):
        input="""int main(){
            string t[00000010];
            t = "abc\\nabc";
            d = "def\tabc";
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_stringlit89(self):
        input="""int main(){
            string t[00000010];
            t = "abc\\nabc";
            d = "def\\tabc";
            e = "ghk\rabc";
        }"""
        expect="ghk"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_stringlit90(self):
        input="""int main(){
            string t[00000010];
            t = "abc\\nabc";
            d = "def\\tabc";
            e = "ghk\\rabc";
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_stringlit91(self):
        input="""int main(){
            string t[00000010];
            t = "abc\\nabc";
            d = "def\\tabc";
            e = "ghk\\rabc";
            w = "xyz\\abc";
        }"""
        expect="xyz\\a"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_stringlit92(self):
        input="""int main(){
            string t[00000010];
            t = "abc\\nabc";
            d = "def\\tabc";
            e = "ghk\\rabc";
            w = "xyz\\";
        }"""
        expect='xyz\\";';
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_stringlit93(self):
        input="""int main(){
            string t[00000010];
            t = "abc\\nabc";
            d = "def\\tabc";
            e = "ghk\\rabc";
            w = "xyz\\ ";
        }"""
        expect="xyz\ ";
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_stringlit94(self):
        input="""int main(){
            string t[00000010];
            t = "abc\\nabc";
            d = "def\\tabc";
            e = "ghk\\rabc";
            w = "xyz; abc";
        }"""
        expect="successful";
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_stringlit95(self):
        input="""int main(){
            string t[00000010];
            t = "abc\\nabc";
            d = "def\\tabc";
            e = "ghk\\rabc";
            w = "xyz"; abc";
        }"""
        expect=";";
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_stringlit96(self):
        input="""int main(){
            string t[00000010];
            t = "abc\\nabc";
            d = "def\\tabc";
            e = "ghk\\rabc";
            w = "xyz\fabc";
        }"""
        expect="successful";
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_stringlit97(self):
        input="""int main(){
            string t[00000010];
            t = "abc\\nabc";
            d = "def\\tabc";
            e = "ghk\\rabc";
            w = "xyz\babc";
        }"""
        expect="successful";
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_stringlit98(self):
        input="""int main(){
            x="abc\\";
        }"""
        expect="""abc\\";"""
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_all99(self):
        input="""int main()
        {
            int i, j, num, arr[250], swap;
            printf("Please enter the number of elements\\n");
            scanf("%d", num);
            printf("Enter %d numbers\\n", num);
            for (i = 0; i < num; i=i+1)
                scanf("%d", arr[i]);
            for (i = 0;i< (num - 1); i=i+1)
            {
                for (j = 0 ; j < num - i - 1; j=j+1)
                {
                    if (arr[j] > arr[j+1]) 
                    {
                    swap     = arr[j];
                    arr[j]   = arr[j+1];
                    arr[j+1] = swap;
                    }
                }
            }
            printf("Bubble sorting in ascending order:\\n");
            for ( i = 0 ; i < num ; i=i+1 )
                printf("%d\\n", arr[i]);
            return 0;
            //i<(num-1);
        }"""
        expect="""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,299))
    
    def test_all300(self):
        input="""void main()
        {
            clrscr();
            int decnum, rem, quot;
            int i, j, octnum[100];
            printf("Enter any decimal number : ");
            scanf("%ld",decnum);
            quot=decnum;
            do{
                octnum[i+1]=quot%8;
                quot=quot/8;
            }while(quot!=0);
            
            printf("Equivalent octal value of %d is : \\n",decnum);
            for(j=i-1; j>0; j=j-1)
            {
                printf("%d",octnum[j]);
            }
            getch();
        }"""
        expect="""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,300))
    