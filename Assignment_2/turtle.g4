/**
 * Define a grammar called turtle

grammar turtle;
r  : 'turtle' ID ;         // match keyword hello followed by an identifier
ID : [a-z]+ ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
*/

grammar turtle;

start: expr | <EOF>;//end of file

expr
	: 'turtle' x_cord=NUMBER y_cord=NUMBER #drawlineExpr
	| 'print' x_cord=NUMBER y_cord=NUMBER #printlineExpr
	;

NUMBER: ('0' .. '9') + ('.' ('0' .. '9')+)?;

WS : [ \r\n\t]+ -> skip;
