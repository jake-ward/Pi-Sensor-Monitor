setTimeout(function myTimer(){
		var d = new Date();
		document.getElementById("demo").innerHTML = d.toLocaleTimeString();
		setTimeout(myTimer, 1000);
	}, 1000);