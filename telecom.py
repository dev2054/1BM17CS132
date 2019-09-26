class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self._phoneno=phoneno
        self._called_no=called_no
        self._duration=duration
        self._call_type=call_type
    def print1(self):
        print(self._phoneno,' ', self._called_no,' ', self._duration,' ', self._call_type,' ') 
class Util:
    def __init__(self):
        self.list_of_call_objects=None
    def parse_customer(self,list_of_call_string):
        self.list_of_call_objects=[]
        for i in list_of_call_string:
            phoneno,called_no,duration,call_type=map(str,i.split(","))
            self.list_of_call_objects.append(CallDetail(phoneno,called_no,duration,call_type))
            c1=CallDetail(phoneno,called_no,duration,call_type)
            c1.print1()
call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'
list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)
