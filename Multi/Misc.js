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
