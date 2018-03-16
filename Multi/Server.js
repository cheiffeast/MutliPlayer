var io = require("socket.io")();

// Globals
var players = [];
var SleepTimer = 1 / 120;

io.on("connection", function(socket){
	uid = parseInt(Math.random() * 1000000);	
	socket.uid = uid;	
	players.push([uid, [0, 0], [0, 0, 0], 20]);
	
	
	
	console.log("Players : " + String(players.length));
	
	socket.emit("uid", socket.uid);
	socket.emit("setup", {"sleep": SleepTimer});
	

	socket.on("disconnect", function(){
		findPlayer(socket.uid, function(index){
			if(index != null){
				players.splice(index, 1);
			}			
		});
		console.log("Players : " + String(players.length));
	});
	
	socket.on("tickReply", function(data){
		findPlayer(socket.uid, function(index){
			if(index != null){
				players[index][1] = data.position;
				players[index][2] = data.color;
				players[index][3] = data.size;
			}
		});		
	});
	
	
});


setInterval(function(){
	io.sockets.emit("tick", players);
	
}, 1000 / 120);

function findPlayer(uid, callback){
	for(i = 0; i < players.length; i++){
			if(players[i][0] == uid){
				callback(i);
			}
	}
	
	callback(null);
}


io.listen(3000);
