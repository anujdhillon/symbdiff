from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
        'Differentiate': '/differentiate/'
		}

	return Response(api_urls)

@api_view(["POST"])
def differentiate(input):
    try:
        fx_obj = expr(input.data['functiondata'])
        fprimex_obj = fx_obj.deriv('x')
        fprimex_str = fprimex_obj.prettyprint()
        fprimex = {'solution': fprimex_str}
        return JsonResponse(fprimex,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

# Create your views here.
class expr:

    def __init__(self, S, Nd=None):
        if (Nd):
            self.expr = Nd
        else:
            (e, n) = self.parse(S)
            self.expr = e

    class Node:
        def __init__(self, d):
            self.left = None
            self.right = None
            self.data = d

        def toString(self):
            if (self.left and self.right):
                left = self.left.toString()
                right = self.right.toString()
                opr = self.data
                if opr == '+':
                    if left == "0":
                        return right
                    elif right == "0":
                        return left
                if opr == '*':
                    if left == "0" or right == "0":
                        return "0"
                    if left == "1":
                        return right
                    if right == "1":
                        return left
                if opr == 'log':
                    if left == "0":
                        return "0"
                    if right == "1":
                        return "0"
                    if right == "e":
                        return left
                if opr == '-':
                    if right == "0":
                        return left
                    if left == "0":
                        return "-" + right
                if opr == '/':
                    if right == "0":
                        raise Exception("Cantdividebyzero")
                    if left == "0":
                        return "0"

                return "(" + left + " " + opr + " " + right + ")"

            else:
                return self.data

    def prettyprint(self):
        s = self.expr.toString()
        return s

    def parse(self, S):
        l = len(S)
        if (S[0] == "("):
            (left, n) = self.parse(S[1:l - 2])
            opr = S[n + 1]
            (right, m) = self.parse(S[n + 2:l - 1])
            expr = self.Node(opr)
            expr.left = left
            expr.right = right
            return (expr, n + m + 3)
        elif S[0].isdigit():
            i = 0
            while ((i < l) and (S[i].isdigit() or (S[i] == "."))):
                i = i + 1
            num = S[0:i]
            expr = self.Node(num)
            return (expr, i)
        elif S[0].isalpha():
            i = 0
            while ((i < l) and S[i].isalpha()):
                i = i + 1
            var = S[0:i]
            expr = self.Node(var)
            return (expr, i)
        else:
            return Exception("Invalid input")

    def constant(self):
        if self.expr.data[0].isdigit():
            return True
        else:
            return False

    def variable(self):
        if self.expr.data[0].isalpha():
            return True
        else:
            return False

    def samevariable(self, x):
        if (self.expr.data == x):
            return True
        else:
            return False

    def sum(self):
        if (self.expr.data == '+'):
            return True
        else:
            return False

    def product(self):
        if (self.expr.data == '*'):
            return True
        else:
            return False

    def division(self):
        if (self.expr.data == '/'):
            return True
        else:
            return False

    def diff(self):
        if (self.expr.data == '-'):
            return True
        else:
            return False

    def power(self):
        if (self.expr.data == '^'):
            return True
        else:
            return False

    def addend(self):
        left = self.expr.left
        return expr("", left)

    def augend(self):
        right = self.expr.right
        return expr("", right)

    def val(self):
        data = self.expr.data
        return expr("", data)

    def makesum(self, e1, e2):
        e = self.Node("+")

        # Original
        # e.left = e1
        # e.right = e2

        # Modified
        e.left = e1.expr
        e.right = e2.expr
        return expr("", e)

    def makeproduct(self, e1, e2):
        e = self.Node("*")
        e.left = e1.expr
        e.right = e2.expr
        return expr("", e)

    def makedivision(self, e1, e2):
        e = self.Node("/")
        e.left = e1.expr
        e.right = e2.expr
        return expr("", e)

    def makediff(self, e1, e2):
        e = self.Node("-")
        e.left = e1.expr
        e.right = e2.expr
        return expr("", e)

    def makepower(self, e1, e2):
        e = self.Node("^")
        e.left = e1.expr
        e.right = e2.expr
        return expr("", e)

    def makelog(self, e1, e2):
        e = self.Node("log")
        e.left = e1.expr
        e.right = e2.expr
        return expr("", e)

    def deriv(self, x):
        if self.constant():
            return expr("0")
        if self.variable():
            if self.samevariable(x):
                return expr("1")
            else:
                return expr("0")
        elif self.sum():
            e1 = self.addend()
            e2 = self.augend()
            return self.makesum(e1.deriv(x), e2.deriv(x))
        elif self.diff():
            e1 = self.addend()
            e2 = self.augend()
            return self.makediff(e1.deriv(x), e2.deriv(x))
        elif self.product():
            e1 = self.addend()
            e2 = self.augend()
            return (self.makesum(self.makeproduct(e2, e1.deriv(x)), self.makeproduct(e1, e2.deriv(x))))
        elif self.division():
            e1 = self.addend()
            e2 = self.augend()
            return (
                self.makedivision(self.makediff(self.makeproduct(e2, e1.deriv(x)), self.makeproduct(e1, e2.deriv(x))),
                                  self.makeproduct(e2, e2)))
        elif self.power():
            e1 = self.addend()
            e2 = self.augend()
            return self.makeproduct(self.makepower(e1, e2),
                                    self.makesum(self.makeproduct(self.makedivision(e2, e1), e1.deriv(x)),
                                                 self.makelog(e2.deriv(x), e1)))
        else:
            raise Exception("DontKnowWhatToDo!")




