const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
const name = document.getElementById('name');
const mobile = document.getElementById('mobile');
const state = document.getElementById('state');
const date = document.getElementById('date');
const form = document.getElementById('form');
const status = false;


signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

// signInButton.addEventListener('click', () => {
// 	container.classList.remove("right-panel-active");
// });

name.addEventListener('input',()=>{
	
});

mobile.addEventListener('input',()=>{

});

state.addEventListener('input',()=>{
	console.log("Hello");
});

/* Capture Code*/
function startcamera()
{
	var player = document.getElementById('player');
	var snapshotCanvas = document.getElementById('snapshot');
	var captureButton = document.getElementById('capture');

	var x=document.getElementById('cam');
	x.style.display="flex";

	var handleSuccess = function(stream) {
	  // Attach the video stream to the video element and autoplay.
	  player.srcObject = stream;
	};
  
	captureButton.addEventListener('click', function() {
	  var context = snapshot.getContext('2d');
	  // Draw the video frame to the canvas.
	  context.drawImage(player, 0, 0, snapshotCanvas.width,
		  snapshotCanvas.height);
	//   console.log(context.canvas.toDataURL());
	var fullQuality = snapshotCanvas.toDataURL('image/jpeg', 1.0);
	
	document.getElementById('image').href=fullQuality;
	console.log();
	});

	navigator.mediaDevices.getUserMedia({video: true})
		.then(handleSuccess);
	  
}
