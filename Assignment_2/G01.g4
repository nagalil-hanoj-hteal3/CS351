grammar G01;
//grammar G28;

start: expr | <EOF>;//end of file

expr
	: 'G01' x_cord=NUMBER y_cord=NUMBER #oneDrawExprUsingG01
	| 'G28' a_cord=NUMBER b_cord=NUMBER #anotherDrawExprUsingG28
	| 'F' c_cord=NUMBER d_cord=NUMBER #lastDrawExprUsingF
	| 'print' x_cord=NUMBER y_cord=NUMBER #printForAllGrammarCodes
	;

NUMBER: ('0' .. '9') + ('.' ('0' .. '9')+)?;

WS : [ \r\n\t]+ -> skip;
