$(document).ready(function(){
		var bouton=document.getElementById('confirmation') ;
		bouton.addEventListener("click", affiche, false) ;

	function affiche() {
		var chpsCommune=document.getElementById('commune');
		var chpsActi=document.getElementById('activite');
		var acti = chpsActi.value;
		var commune =chpsCommune.value;
		if((commune!=null)&&(acti!=null)){
		//TODO remplir les destinations de REST
			//call(../,chpsCommune.val(),chpsActi.val());
		}else if(commune!=null){
			//call(../,chpsCommune.val());
		}else if(acti!=null){
			 var test = call("../services/Activite/res_activites/activite()",chpsActi.val());
			 $('body').append("<p>"+test+"<p>");
		}else{
			window.alert("Veuillez remplir au moins un des champs");
		}
	}
});
