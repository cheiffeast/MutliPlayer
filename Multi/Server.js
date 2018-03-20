var io = require("socket.io")();
var misc = require("./Misc.js");

// Globals
var players = [];
var SleepTimer = 1 / 120;
var objects = [];
var world = misc.loadWorld("worlds/example.world", function(data){
	objects = data;
});





io.on("connection", function(socket){

	socket.uid = misc.generateUID();
	players.push([socket.uid, [0, 0], [0, 0, 0], 20]);
	misc.log("New player #" + String(socket.uid) + " (" + String(players.length) + ")");



	socket.emit("setup", {"sleep": SleepTimer, "uid": socket.uid});


	socket.on("disconnect", function(){
		misc.findPlayer(socket.uid, players, function(index){
			if(index != null){
				players.splice(index, 1);
			}
		});
		misc.log("Player disconnected #" + String(socket.uid) + " (" + String(players.length) + ")");
	});

	socket.on("tickReply", function(data){
		misc.findPlayer(socket.uid, players, function(index){
			if(index != null){
				players[index][1] = data.position;
				players[index][2] = data.color;
				players[index][3] = data.size;
			}
		});
	});


});

setInterval(function(){
	io.sockets.emit("tick", {"players": players, "objects": objects});

}, 1000 / 120);


io.listen(3000);
misc.log("Server started");
