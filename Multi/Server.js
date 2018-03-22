var io = require("socket.io")();
var misc = require("./Misc.js");

// Globals
var players     = [],
		objects     = [],
		sockets     = [],
    sleepTimer  = 1 / 120,
 		maxObjs     = 100,
	  ticks       = 0,
    worldUpdate = 0;

misc.loadWorld("worlds/example.world", function(data){
	objects = data;
});





io.on("connection", function(socket){
	// Add the socket to the socket list
	sockets.push(socket);

	// Generate UID and then add to the player list
	socket.uid = misc.generateUID();
	players.push([socket.uid, [0, 0, 20, 20], [0, 0, 0], Date.now()]);

	// Print to the console and then send the user some information about the server
	misc.log("New player #" + String(socket.uid) + " (" + String(players.length) + ")");
	socket.emit("setup", {"sleep": sleepTimer, "uid": socket.uid});


	socket.on("disconnect", function(){
		misc.findPlayer(socket.uid, players, function(index){
			if(index != null){
				players.splice(index, 1);
			}
		});
		sockets.splice(sockets.indexOf(socket), 1);
		misc.log("Player disconnected #" + String(socket.uid) + " (" + String(players.length) + ")");
	});

	socket.on("tickReply", function(data){
		misc.findPlayer(socket.uid, players, function(index){
			if(index != null){
				players[index][1] = data.position;
				players[index][2] = data.color;
				players[index][3] = Date.now();
			}
		});
	});

	socket.on("addProjectile", function(data){
		if(data.velocity[0] > 5 || data.velocity[1] > 5){
			misc.log("Unaccepted projectile from user #" + String(socket.uid));
		}
		else{
			objects.push([data.position, data.color, data.velocity]);
		}
	});


});

setInterval(function(){
	for(var i in sockets){
		misc.findPlayer(sockets[i].uid, players, function(index){
			if(index != -1){
				try{
					misc.generateObjectList(players[i][1], objects, function(objs){
						sockets[i].emit("tick", {"players": players, "objects": objs})
					});
				}
				catch(err){
					misc.log("Tried to update a player that is not there");
				}
			}
		});
	}

	for(var i in objects){
		objects[i][0] = [objects[i][0][0] + objects[i][2][0],
										 objects[i][0][1] + objects[i][2][1],
									 	 objects[i][0][2], objects[i][0][3]];
	}
	ticks += 1;

}, 1000 / 120);

setInterval(function(){
	misc.loadWorld("worlds/example.world", function(data){
		//objects = data;
		additional = objects.splice(data.length, objects.length);
		objects = data.concat(additional.splice(additional.length - maxObjs, maxObjs));
		if(worldUpdate % 120 == 0){
			misc.log("There are " + String(objects.length) + " object(s) in the world");
		}
	});
	worldUpdate += 1;
}, 500);


io.listen(3000);
misc.log("Server started");
