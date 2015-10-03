
$(document).ready(function(){
	$("#limpar").click(function(){
		$(".input input").each(function(){ 
			$(this).attr('value', '')
		})
		$('#resposta').text('')	
	})
})




