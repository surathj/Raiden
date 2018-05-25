var app = require('express')(),
http_server = require('http').Server(app),
io = require('socket.io')(http_server)

var gameState = require('F:/Projects/FYP/Server/game_state')
var dataStr ='';
var max_player_limit = 1;
var players = [];
var players_count = 0;

//status codes
var is_registered = 60;
var game_ready = 80;

sampleFunc = function(socket){
	var spawn = require('child_process').spawn,
	    py = spawn('python', ['F:/Projects/FYP/Server/game_state/attack_generator.py']),
	    data = [1,2,3,4,5,6,7,8,9];
	    dataString = '';

	py.stdout.on('data', function(data){
			console.log("before data write");
			  dataString += data;
			  //return dataString;
			});

		py.stdout.on('end', function(){
			console.log("successful");
			dataStr = dataString;''
			//console.log(dataString);
			io.emit('on_aaa_response', JSON.parse(dataString));
      //io.emit('on_aaa_response', {'server_message':'hello to everyone'})
      
  		  //console.log(dataString);
			  //return dataString;
			});
		//data needs to be stringified for python to recognize it
		py.stdin.write(JSON.stringify(data));
		console.log("inside stdin");	
		py.stdin.end();
		//return dataString;

};

connect_to_ai = function(socket_id, player_profile){
  var spawn = require('child_process').spawn,
  py = spawn('python', ['F:/Projects/FYP/ANN/DataInterface.py']),
  data = [socket_id, player_profile] //[[30, 80.22, 7, 0], [69, 73.55, 8, 1], [50, 50, 5, 1]];
  dataString = ''

  py.stdout.on('data', function(data){
      console.log("before data write");
        dataString += data;
        //return dataString;
      });

    py.stdout.on('end', function(){
      console.log("successful");
      dataStr = dataString;
      console.log(dataString)
      //io.emit('on_aaa_response', JSON.parse(dataString));
      //io.emit('on_aaa_response', {'server_message':'hello to everyone'})
      
        //console.log(dataString);
        //return dataString;
      });
    //data needs to be stringified for python to recognize it
    py.stdin.write(JSON.stringify(data));
    console.log("inside stdin");  
    py.stdin.end();
    //return dataString;

};

/*app.get('/', function(req, res){
	console.log("here");
	sampleFunc();
	console.log(dataString);
  	res.send(JSON.stringify(dataString));
  
});*/

io.on('connection', function(socket){
  console.log('a user connected');
  socket.broadcast.emit('new_player', socket.id)
  //socket.emit('socketID', {id: socket.id});
  //socket.broadcast.emit('new_player', {id: socket.id});
  //socket.emit('get_players', JSON.parse(players));

  //register listener
  //socket.on('register', function(msg){
  console.log("register request");
  if(players.size >= max_player_limit){
    console.log("players full");
    io.emit('reg_data', {'server_message': 'Maximum client number reached'});
  }
  else{
    console.log("pushing player");
    players.push(new player(socket.id, 0, 0));
    players_count += 1;
    console.log(players_count);
    //io.emit('register', {'status': is_registered});
    if(players_count == max_player_limit){
      console.log(players_count);
      status_data = JSON.stringify({'is_registered': is_registered, 'game_ready': game_ready});
      parsed_status_data = JSON.parse(status_data);
      console.log(parsed_status_data);
      //io.emit('reg_data', parsed_status_data);//JSON.parse((is_registered, game_ready))
      sampleFunc(socket);
    }
    else{
      console.log("Waiting for more players to join...");
    }
  }
  //});

  //attack listener
  /*socket.on('attack', function(msg){
  	var jsonstr = JSON.stringify(msg);
  	var parsedObj = JSON.parse(jsonstr); 
    console.log(parsedObj);
    sampleFunc(socket);
    //io.emit('on_aaa_response', {'server_message' : 'Sending attack data'})
    //connect_to_ai();
  });*/

  

  //location listener
  socket.on('player_moved', function(data){
  	data.id = socket.id;
 
  	for(var i = 0; i < players.length; i++){
        if(players[i].id == data.id){
      		players[i].x = data.x;
      		players[i].y = data.y;
      }
  	}
    socket.broadcast.emit('player_moved', (data[0], data[1]));
  });


  //player has finished level
  socket.on('player_profile', function(data){
    console.log("player has finished level");
    console.log(data);
    console.log("about to send to AI");
    connect_to_ai(socket.id, data);
    //connect_to_ai(data);

  });


  //disconnect listener
  socket.on('disconnect', function(){
  	console.log("User disconnected");
  	socket.broadcast.emit('player_disconnected', {'player_id': socket.id});

  	for(var i = 0; i < players.length; i++){
  			if(players[i].id == socket.id){
        players.splice(i, 1);
      }
  	}
  			
  });
  
});



http_server.listen(3000, function(){
	console.log("listening on *: 3000");
});

function player(id, x, y){
	this.id = id;
	this.x = x;
	this.y = y;
  this.class = 0;
}