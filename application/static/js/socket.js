$(document).ready(function() {
	
	namespace = '/';

	var socket = io.connect('http://192.168.0.34:5000' + namespace);

	socket.on('connect', function() {
		console.log('Connection Established!');
		socket.emit('my_event', {data: 'I\'m connected!'});
	});

	socket.on('message', function(msg) {
		console.log('Received Message');
		var nDate = new Date();
		h = check(nDate.getHours());
		m = check(nDate.getMinutes());
		s = check(nDate.getSeconds());
		$('#time').text(h + ':' + m + ':' + s).html();
		
		socket.emit('my_event', {humid: $('#humidity'), temp: $('#temperature')});
		$('#humidity').text(msg.humid).html();
		$('#temperature').text(msg.temp).html();
	});
	
	function check(i) {
		if (i<10) {i = "0" +  i};
		return i;
	}
	
	socket.on('disconnect', function() {
		console.log('User Disconnected');
		socket.disconnect();
		socket.close();
	});
});