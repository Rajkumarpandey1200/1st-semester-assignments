declare 
a int;
b int;
c int;
c=a+b; 
begin
a:=&a;
b:=&b;
dbms_output.put_line('sum of two numb is'||c);
end;
/
