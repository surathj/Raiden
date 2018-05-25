var spawn = require('child_process').spawn,
    py    = spawn('python', ['sample.py']),
    data = [1,2,3,4,5,6,7,8,9],
    dataString = '';

exports.someFunc = function(){
	py.stdout.on('data', function(data){
		console.log("before data write");
		  dataString += data.toString();
		});

	py.stdout.on('end', function(){
		console.log("printing out");
		  console.log('Sum of numbers=', dataString);
		  return dataString;
		});

	py.stdin.write(JSON.stringify(data));
	console.log("ending stdin");	
	py.stdin.end();
};

exports.worker = function(){
	return someFunc()

};