var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var path = require('path');

var dataStr = '';

sampleFunc = function(){
	var spawn = require('child_process').spawn,
	    py = spawn('python', ['F:/Projects/FYP/Server/game_state/sample.py']),
	    data = [1,2,3,4,5,6,7,8,9];
	    dataString = '';

	py.stdout.on('data', function(data){
			console.log("before data write");
			  dataString += data.toString();
			  //return dataString;
			});

		py.stdout.on('end', function(){
			console.log("successful");
			  //console.log(dataString);
			  io.emit('on_aaa_response', dataString)
			  //console.log(dataStr);
			});

		py.stdin.write(JSON.stringify(data));
		console.log("inside stdin");	
		py.stdin.end();
		//return dataString;

		

};


var serversidemsg = 'hello from the server-side'

/*app.get('/', function(req, res){
  res.sendFile(__dirname + '/client.html');
});*/

io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('message', function(msg){
  	var jsonstr = JSON.stringify(msg);
  	var parsedObj = JSON.parse(jsonstr); 
    console.log(parsedObj);
    sampleFunc()
    //console.log(dataStr)
   	//io.emit('on_aaa_response', parsedObj);
  });
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});