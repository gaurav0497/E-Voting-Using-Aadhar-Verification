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

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

name.addEventListener('input',()=>{
	
});

mobile.addEventListener('input',()=>{

});

state.addEventListener('input',()=>{

});
