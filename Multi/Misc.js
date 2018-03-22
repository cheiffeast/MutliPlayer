var fs = require("fs");

var exports = module.exports = {};

exports.findPlayer = function(uid, players, callback){
	for(i = 0; i < players.length; i++){
			if(players[i][0] == uid){
				callback(i);
			}
	}
	callback(null);
}

exports.log = function(msg){
	var time = new Date();
	message = "[" + time.toTimeString().split(" ")[0] + "]: " + msg;
	console.log(message);
}

exports.generateUID  = function(){
  uid = parseInt(Math.random() * 1000000000);
  return uid;

}

exports.loadWorld = function(worldFile, callback){
	fs.readFile(worldFile, "utf-8", function(err, data){
		if(err){
			console.log(err);
		}
		else{
			array = [];
			pieces = data.split('\n');

			for(i = 0; i < pieces.length - 1; i++){
				piece = JSON.parse(pieces[i]);
				array.push([piece.position, piece.color, piece.velocity]);
			}

			callback(array);
		}
	});
}

exports.generateObjectList = function(pos, objects, callback){
	pobjs = [];
	for(var i in objects){
		dist = Math.pow(pos[0] - objects[i][0][0], 2) + Math.pow(pos[1] - objects[i][0][1], 2);
		if(dist < 1000000){
			pobjs.push(objects[i]);
		}
	}
	callback(pobjs);
}
