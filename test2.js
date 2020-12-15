/* 
  var a,b,c;
  function sub1() {
    var b,c,e;
    b = 5
    console.log(b)
  }
  function sub3(subx) {
    var b=4,e;
    console.log(b)
    subx();
    a = b + e;
  }
  b = 4
  sub3(sub1)
 */

function main() 
{ 
    x = 1     
	function f() 
    { 
        console.log(x) 
    } 
    function g(h) 
    { 
        x = 2         
		h() 
    } 
    function j() 
    { 
        x = 3         
		g(f) 
    } 
    j() 
}
main()  