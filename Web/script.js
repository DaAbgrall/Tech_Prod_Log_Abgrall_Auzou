$(document).ready(function(){
	function init(){
		var bouton=document.getElementById('confirmation') ;
		el.addEventListener("click", affiche, false) ;
	}

	function affiche() {
		var chpsCommune=document.getElementById('commune');
		var chpsActi=document.getElementById('activite');
		if((chpsCommune.val()!=null)&&(chpsActi.val()!=null)){
		//TODO remplir les destinations de REST
			call(../,chpsCommune.val(),chpsActi.val());//ICI
		}else if(chpsCommune.val()!=null){
			call(../,chpsCommune.val());//ICI
		}else if(chpsActi.val()!=null){
			call(../,chpsActi.val());//ICI
		}else{
			window.alert("Veuillez remplir au moins un des champs")
		}
	}
}
